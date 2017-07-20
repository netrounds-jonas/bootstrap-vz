from qemuvolume import QEMUVolume


class Qcow2Volume(QEMUVolume):

    extension = 'qcow2'
    qemu_format = 'qcow2'

# vi: ts=4 expandtab
