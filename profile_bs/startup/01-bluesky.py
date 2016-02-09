from functools import partial
from bluesky.standard_config import *
from bluesky.scans import *
from bluesky.callbacks import *
from bluesky.broker_callbacks import *
from bluesky.suspenders import *

# Set up required metadata fields with dummy values for now.
gs.RE.md['group'] = ''
gs.RE.md['config'] = {}
gs.RE.md['beamline_id'] = 'SRX'

def print_scan_ids(start_doc):
    print("Transient Scan ID: {0}".format(start_doc['scan_id']))
    print("Persistent Unique Scan ID: '{0}'".format(start_doc['uid']))

gs.RE.subscribe('start', print_scan_ids)
# RE.logbook = olog_wrapper(olog_client, ['Data Acquisitioning'])

checklist = partial(basic_checklist, ca_url='http://xf05id-ca1.cs.nsls2.local:4800',
                    disk_storage=[('/', 1e9)],
                    # pv_names=['XF:23ID1-ES{Dif-Ax:SY}Pos-SP'],
                    pv_conditions=[('XF:05ID-PPS{Sh:WB}Sts:Cls-Sts', 'front-end shutter is open', assert_pv_equal, 0),
                                   ('SR:C03-BI{DCCT:1}I:Real-I', 'beam current is above 50mA', assert_pv_greater, 50),]
                   )

PVSuspendFloor(gs.RE, 'SR:C03-BI{DCCT:1}I:Real-I', 50, resume_thresh=100, sleep=300)
PVSuspendBoolHigh(gs.RE, 'XF:05ID-PPS{Sh:WB}Sts:Cls-Sts', 50, sleep=300)

