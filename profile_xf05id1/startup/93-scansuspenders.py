# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:57:20 2016

Define suspenders that will be loaded

@author: xf05id1
"""
from bluesky.suspenders import SuspendFloor, SuspendCeil, SuspendBoolHigh

susp_rc = SuspendFloor(ring_current, 50, resume_thresh=149, sleep=10*60)

cryo_v19 = EpicsSignal('XF:05IDA-UT{Cryo:1-IV:19}Sts-Sts')
susp_cryo = SuspendCeil(cryo_v19, 0.8, resume_thresh=0.2, sleep=20*60)


susp_shut_fe = SuspendBoolHigh(shut_fe.close_status, sleep = 2*60)
susp_shut_a = SuspendBoolHigh(shut_a.close_status, sleep = 10)
sups_shut_b = SuspendBoolHigh(shut_b.close_status, sleep = 10)

dcm_bragg_temp = EpicsSignal('XF:05IDA-OP:1{Mono:HDCM-Ax:P}T-I')
susp_dcm_bragg_temp = SuspendCeil(dcm_bragg_temp, 120, resume_thresh=70, 
                                  sleep = 10)

# RE.install_suspender(susp_rc)
# RE.install_suspender(susp_cryo)
# RE.install_suspender(susp_shut_a)
# RE.install_suspender(susp_shut_b)
# RE.install_suspender(susp_shut_fe)
# RE.install_suspender(susp_dcm_bragg_temp)
