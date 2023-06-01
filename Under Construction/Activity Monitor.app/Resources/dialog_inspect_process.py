import os
import datetime
import socket
import sys

import psutil

from PyQt5.QtCore import Qt, QFileInfo
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QFileIconProvider,

)
from PyQt5.QtWidgets import QWidget
from dialog_inspect_process_ui import Ui_InspectProcess

from utility import get_process_application_name
from utility import bytes2human

ACCESS_DENIED = ''
NON_VERBOSE_ITERATIONS = 4
RLIMITS_MAP = {
    "RLIMIT_AS": "virtualmem",
    "RLIMIT_CORE": "coredumpsize",
    "RLIMIT_CPU": "cputime",
    "RLIMIT_DATA": "datasize",
    "RLIMIT_FSIZE": "filesize",
    "RLIMIT_MEMLOCK": "memlock",
    "RLIMIT_MSGQUEUE": "msgqueue",
    "RLIMIT_NICE": "nice",
    "RLIMIT_NOFILE": "openfiles",
    "RLIMIT_NPROC": "maxprocesses",
    "RLIMIT_NPTS": "pseudoterms",
    "RLIMIT_RSS": "rss",
    "RLIMIT_RTPRIO": "realtimeprio",
    "RLIMIT_RTTIME": "rtimesched",
    "RLIMIT_SBSIZE": "sockbufsize",
    "RLIMIT_SIGPENDING": "sigspending",
    "RLIMIT_STACK": "stack",
    "RLIMIT_SWAP": "swapuse",
}


class InspectProcess(QWidget, Ui_InspectProcess):
    def __init__(self, parent=None, process=None):
        super(InspectProcess, self).__init__(parent)
        Ui_InspectProcess.__init__(self)
        self.setupUi(self)
        self.process = process
        self.open_files_model = QStandardItemModel()

        self.buttonQuit.clicked.connect(self.quit)
        self.setWindowTitle(f"{get_process_application_name(self.process)} ({self.process.pid})")

        self.sample_text = ""

    def quit(self):
        self.close()

    def add_to_sample_text(self, a, b):
        if a != "":
            a = f"{a.upper()}:"
        self.sample_text += "%-13s %s\n" % (a, b)

    def str_ntuple(self, nt, convert_bytes=False):
        if nt == ACCESS_DENIED:
            return ""
        if not convert_bytes:
            return ", ".join(["%s=%s" % (x, getattr(nt, x)) for x in nt._fields])
        else:
            return ", ".join(["%s=%s" % (x, bytes2human(getattr(nt, x))) for x in nt._fields])

    def run(self, verbose=False):
        try:
            proc = self.process
            pinfo = proc.as_dict(ad_value=ACCESS_DENIED)
        except psutil.NoSuchProcess as err:
            sys.exit(str(err))

        # collect other proc info
        with proc.oneshot():
            try:
                parent = proc.parent()
                if parent:
                    parent = '(%s)' % parent.name()
                else:
                    parent = ''
            except psutil.Error:
                parent = ''
            try:
                pinfo['children'] = proc.children()
            except psutil.Error:
                pinfo['children'] = []
            if pinfo['create_time']:
                started = datetime.datetime.fromtimestamp(
                    pinfo['create_time']).strftime('%Y-%m-%d %H:%M')
            else:
                started = ACCESS_DENIED

        # here we go
        # Title
        self.add_to_sample_text('pid', pinfo['pid'])
        self.add_to_sample_text('name', pinfo['name'])


        # Parent
        self.add_to_sample_text('parent', '%s %s' % (pinfo['ppid'], parent))
        self.parent_process_value.setText('%s %s' % (pinfo['ppid'], parent))

        self.add_to_sample_text('exe', pinfo['exe'])
        self.add_to_sample_text('cwd', pinfo['cwd'])
        self.add_to_sample_text('cmdline', ' '.join(pinfo['cmdline']))
        self.add_to_sample_text('started', started)

        # CPU Time
        cpu_tot_time = datetime.timedelta(seconds=sum(pinfo['cpu_times']))
        cpu_tot_time = "%s:%s.%s" % (
            cpu_tot_time.seconds // 60 % 60,
            str((cpu_tot_time.seconds % 60)).zfill(2),
            str(cpu_tot_time.microseconds)[:2])
        self.cpu_time_value.setText(f"{cpu_tot_time}")

        self.add_to_sample_text('cpu-times', self.str_ntuple(pinfo['cpu_times']))
        if hasattr(proc, "cpu_affinity"):
            self.add_to_sample_text("cpu-affinity", pinfo["cpu_affinity"])
        if hasattr(proc, "cpu_num"):
            self.add_to_sample_text("cpu-num", pinfo["cpu_num"])

        self.add_to_sample_text('memory', self.str_ntuple(pinfo['memory_full_info'], convert_bytes=True))
        self.add_to_sample_text('memory %', round(pinfo['memory_percent'], 2))
        if pinfo['memory_full_info']:
            if hasattr(pinfo['memory_full_info'], "uss"):
                self.unique_set_size_value.setText(f"{bytes2human(pinfo['memory_full_info'].uss)}")
            else:
                self.unique_set_size_label.hide()
                self.unique_set_size_value.hide()

            if hasattr(pinfo['memory_full_info'], "vms"):
                self.virtual_memory_size_value.setText(f"{bytes2human(pinfo['memory_full_info'].vms)}")
            else:
                self.virtual_memory_size_value.hide()
                self.virtual_memory_size_label.hide()

            if hasattr(pinfo['memory_full_info'], "rss"):
                self.resident_set_size_value.setText(f"{bytes2human(pinfo['memory_full_info'].rss)}")
            else:
                self.resident_set_size_value.hide()
                self.resident_set_size_label.hide()

            if hasattr(pinfo['memory_full_info'], "shared"):
                self.shared_memory_size_value.setText(f"{bytes2human(pinfo['memory_full_info'].shared)}")
            else:
                self.shared_memory_size_value.hide()
                self.shared_memory_size_label.hide()

            if hasattr(pinfo['memory_full_info'], "text"):
                self.text_resitent_set_size_value.setText(f"{bytes2human(pinfo['memory_full_info'].text)}")
            else:
                self.text_resitent_set_size_value.hide()
                self.text_resitent_set_size_label.hide()

            if hasattr(pinfo['memory_full_info'], "data"):
                self.data_resident_set_size_value.setText(f"{bytes2human(pinfo['memory_full_info'].data)}")
            else:
                self.data_resident_set_size_value.hide()
                self.data_resident_set_size_label.hide()

            if hasattr(pinfo['memory_full_info'], "swap"):
                self.swapped_size_value.setText(f"{bytes2human(pinfo['memory_full_info'].swap)}")
            else:
                self.swapped_size_value.hide()
                self.swapped_size_label.hide()

            if hasattr(pinfo['memory_full_info'], "lib"):
                self.shared_libraries_size_value.setText(f"{bytes2human(pinfo['memory_full_info'].lib)}")
            else:
                self.shared_libraries_size_value.hide()
                self.shared_libraries_size_label.hide()

            if hasattr(pinfo['memory_full_info'], "pss"):
                self.proportional_set_size_value.setText(f"{bytes2human(pinfo['memory_full_info'].pss)}")
            else:
                self.proportional_set_size_value.hide()
                self.proportional_set_size_label.hide()

            if hasattr(pinfo['memory_full_info'], "stack"):
                self.stack_size_value.setText(f"{pinfo['memory_full_info'].stack}")
            else:
                self.stack_size_label.hide()
                self.stack_size_value.hide()

        # User
        self.add_to_sample_text('user', pinfo['username'])
        if psutil.POSIX:
            self.add_to_sample_text('uids', self.str_ntuple(pinfo['uids']))
            self.user_value.setText(f"{pinfo['uids'].effective} ({pinfo['username']})")

        # Group
        if psutil.POSIX:
            self.add_to_sample_text('gids', self.str_ntuple(pinfo['gids']))
            self.process_group_id_value.setText(f"{self.str_ntuple(pinfo['gids'])}")

        # CPU
        self.cpu_percent_value.setText(f"{proc.cpu_percent(interval=1)}")

        # Status
        self.status_value.setText(f"{pinfo['status']}")

        # Nice
        self.nice_value.setText(f"{pinfo['nice']}")

        if hasattr(proc, "ionice"):
            try:
                ionice = proc.ionice()
            except psutil.Error:
                pass
            else:
                if psutil.WINDOWS:
                    self.add_to_sample_text("ionice", ionice)
                else:
                    self.add_to_sample_text("ionice", "class=%s, value=%s" % (
                        str(ionice.ioclass), ionice.value))

        # Threads Number
        self.threads_number_value.setText(f"{pinfo['num_threads']}")

        if psutil.POSIX:
            self.file_descriptors_value.setText(f"{pinfo['num_fds']}")

        if 'io_counters' in pinfo:
            self.add_to_sample_text('I/O', self.str_ntuple(pinfo['io_counters'], convert_bytes=True))

        if 'num_ctx_switches' in pinfo:
            # self.add_to_sample_text("ctx-switches", self.str_ntuple(pinfo['num_ctx_switches']))
            self.context_switches_value.setText(f"{self.str_ntuple(pinfo['num_ctx_switches'])}")
        else:
            pass

        if pinfo['children']:
            template = "%-6s %s"
            self.add_to_sample_text("children", template % ("PID", "NAME"))
            for child in pinfo['children']:
                try:
                    self.add_to_sample_text('', template % (child.pid, child.name()))
                except psutil.AccessDenied:
                    self.add_to_sample_text('', template % (child.pid, ""))
                except psutil.NoSuchProcess:
                    pass

        # Open Files
        if pinfo['open_files']:
            self.add_to_sample_text('open-files', 'PATH')
            self.open_files_model = QStandardItemModel()
            headers = []

            for i, file in enumerate(pinfo['open_files']):
                row = []
                if hasattr(file, "path"):
                    item = QStandardItem(f"{file.path}")
                    item.setData(file.path)
                    item.setIcon(QFileIconProvider().icon(QFileInfo(file.path)))
                    row.append(item)
                    if "Path" not in headers:
                        headers.append("Path")

                if hasattr(file, "fd"):
                    item = QStandardItem(f"{file.fd}")
                    item.setData(file.fd)
                    row.append(item)
                    if "Fd" not in headers:
                        headers.append("Fd")

                if hasattr(file, "position"):
                    item = QStandardItem(f"{file.position}")
                    item.setData(file.position)
                    row.append(item)
                    if "Position" not in headers:
                        headers.append("Position")

                if hasattr(file, "mode"):
                    item = QStandardItem(f"{file.mode}")
                    item.setData(file.mode)
                    if f"{file.mode}" == "r" or f"{file.mode}" == "rt":
                        item.setToolTip("<html><head/><body><p>Open for reading text</p></body></html>\n")
                    elif f"{file.mode}" == "r+" or f"{file.mode}" == "r+b":
                        item.setToolTip("<html><head/><body><p>Open the file with no truncation</p></body></html>\n")
                    elif f"{file.mode}" == "w":
                        item.setToolTip("<html><head/><body><p>Open for writing, truncating the file "
                                        "first</p></body></html>\n")
                    elif f"{file.mode}" == "w+" or f"{file.mode}" == "w+b":
                        item.setToolTip("<html><head/><body><p>Open and truncate the file</p></body></html>\n")
                    elif f"{file.mode}" == "a":
                        item.setToolTip("<html><head/><body><p>Open for writing, appending to the end of file if it "
                                        "exists</p></body></html>\n")
                    elif f"{file.mode}" == "b":
                        item.setToolTip("<html><head/><body><p>Binary mode</p></body></html>\n")
                    elif f"{file.mode}" == "t":
                        item.setToolTip("<html><head/><body><p>Text mode</p></body></html>\n")
                    elif f"{file.mode}" == "+":
                        item.setToolTip("<html><head/><body><p>Open for updating (reading and "
                                        "writing)</p></body></html>\n")

                    row.append(item)
                    if "Mode" not in headers:
                        headers.append("Mode")

                if hasattr(file, "flags"):
                    item = QStandardItem(f"{file.flags}")
                    row.append(item)
                    if "Flags" not in headers:
                        headers.append("Flags")

                if row:
                    self.open_files_model.appendRow(row)
                self.add_to_sample_text('', file.path)

                self.open_files_model.setHorizontalHeaderLabels(headers)

                self.OpenFileTreeView.setModel(self.open_files_model)

                for header_pos in range(len(self.OpenFileTreeView.header())):
                    self.OpenFileTreeView.resizeColumnToContents(header_pos)
                self.OpenFileTreeView.sortByColumn(0, Qt.AscendingOrder)

        else:
            self.add_to_sample_text('open-files', '')

        # Connections
        num_ports = 0
        if pinfo['connections']:
            connections_model = QStandardItemModel()
            for conn in pinfo['connections']:
                if conn.type == socket.SOCK_STREAM:
                    type = 'TCP'
                elif conn.type == socket.SOCK_DGRAM:
                    type = 'UDP'
                else:
                    type = 'UNIX'
                lip, lport = conn.laddr
                if not conn.raddr:
                    rip, rport = '*', '*'
                else:
                    rip, rport = conn.raddr
                connections_model.appendRow(
                    [
                        QStandardItem(f"{type}"),
                        QStandardItem(f"{lip}:{lport}"),
                        QStandardItem(f"{rip}:{rport}"),
                        QStandardItem(f"{conn.status}"),
                    ]
                )
                # Ports Number
                # if conn.status == psutil.CONN_LISTEN:
                num_ports += 1
            self.ports_value.setText(f"{num_ports}")
            connections_model.setHorizontalHeaderLabels(('Protocol', 'Local Address', 'Remote Address', 'Status'))
            self.ConnectionsTreeView.setModel(connections_model)
            for header_pos in range(len(self.ConnectionsTreeView.header())):
                self.ConnectionsTreeView.resizeColumnToContents(header_pos)
            self.ConnectionsTreeView.sortByColumn(0, Qt.AscendingOrder)


        else:
            self.add_to_sample_text('connections', '')
            self.ports_value.setText(f"{num_ports}")

        if pinfo['threads'] and len(pinfo['threads']) > 1:
            template = "%-5s %12s %12s"
            self.add_to_sample_text('threads', template % ("TID", "USER", "SYSTEM"))
            for i, thread in enumerate(pinfo['threads']):
                self.add_to_sample_text('', template % thread)
            self.add_to_sample_text('', "total=%s" % len(pinfo['threads']))
        else:
            self.add_to_sample_text('threads', '')

        if hasattr(proc, "rlimit"):
            res_names = [x for x in dir(psutil) if x.startswith("RLIMIT")]
            resources = []
            for res_name in res_names:
                try:
                    soft, hard = proc.rlimit(getattr(psutil, res_name))
                except psutil.AccessDenied:
                    pass
                else:
                    resources.append((res_name, soft, hard))
            if resources:
                template = "%-12s %15s %15s"
                self.add_to_sample_text("res-limits", template % ("RLIMIT", "SOFT", "HARD"))
                for res_name, soft, hard in resources:
                    if soft == psutil.RLIM_INFINITY:
                        soft = "infinity"
                    if hard == psutil.RLIM_INFINITY:
                        hard = "infinity"
                    self.add_to_sample_text('', template % (
                        RLIMITS_MAP.get(res_name, res_name), soft, hard))

        if hasattr(proc, "environ") and pinfo['environ']:
            environment_model = QStandardItemModel()

            template = "%-25s %s"
            self.add_to_sample_text("environ", template % ("NAME", "VALUE"))
            for name, value in pinfo['environ'].items():
                row = []
                self.add_to_sample_text("", template % (name, value))
                item = QStandardItem()
                item.setText(f"{name}")
                item.setData(name)
                row.append(item)

                item = QStandardItem()
                item.setText(f"{value}")
                item.setData(value)
                row.append(item)

                if row:
                    environment_model.appendRow(row)

            environment_model.setHorizontalHeaderLabels(["Name", "Value"])

            self.treeViewEnvironement.setModel(environment_model)

            for header_pos in range(len(self.treeViewEnvironement.header())):
                self.treeViewEnvironement.resizeColumnToContents(header_pos)
            self.treeViewEnvironement.sortByColumn(0, Qt.AscendingOrder)

        if pinfo.get('memory_maps', None):
            environment_model = QStandardItemModel()
            headers = []
            for m in proc.memory_maps(grouped=False):
                row = []
                if hasattr(m, "addr"):
                    item = QStandardItem()
                    item.setText(f"{m.addr.split('-')[0].zfill(16)}")
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    row.append(item)
                    if "Address" not in headers:
                        headers.append("Address")

                if hasattr(m, "rss"):
                    item = QStandardItem()
                    item.setText(bytes2human(m.rss))
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    row.append(item)
                    if "RSS" not in headers:
                        headers.append("RSS")

                if hasattr(m, "private"):
                    item = QStandardItem()
                    item.setText(bytes2human(m.private))
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    row.append(item)
                    if "Private" not in headers:
                        headers.append("Private")

                if hasattr(m, "perms"):
                    item = QStandardItem()
                    item.setText(f"{m.perms}")
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    row.append(item)
                    if "Mode" not in headers:
                        headers.append("Mode")

                if hasattr(m, "path"):
                    item = QStandardItem()
                    item.setText(f"{m.path}")
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    item.setIcon(QFileIconProvider().icon(QFileInfo(m.path)))
                    # if os.path.exists(m.path):
                    #     item.setIcon(QFileIconProvider().icon(QFileInfo(m.path)))
                    # else:
                    #     item.setIcon(QIcon.fromTheme("system-run"))
                    row.append(item)
                    if "Mapping" not in headers:
                        headers.append("Mapping")

                if row:
                    environment_model.appendRow(row)
            environment_model.setHorizontalHeaderLabels(headers)

            self.MapsTreeView.setModel(environment_model)

            for header_pos in range(len(self.MapsTreeView.header())):
                self.MapsTreeView.resizeColumnToContents(header_pos)

            self.MapsTreeView.sortByColumn(0, Qt.DescendingOrder)

        print(self.sample_text)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = InspectProcess(process=psutil.Process(os.getpid()))
    win.run()
    win.show()
    sys.exit(app.exec())
