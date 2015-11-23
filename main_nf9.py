#!/usr/bin/env python2
#
#  pygennf: UDP packets producer with scapy.
#  Copyright (C) 2015-2016  Ana Rey <anarey@redborder.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import scapy
from scapy.all import *
from rb_netflow import *

# Netflow9

header_v9 = Netflow_Headerv9(version=9, count= 2, SysUptime= 27.027095000, Timestamp=1392292623, FlowSequence= 0,SourceId= 243)


flowSet_header_v9 = FlowSet_Header_v9(FlowSet_id= 0, FlowSet_length=80)


flowset_id_v9 = FlowTemplate_ID_v9(template_id=258,count=18)

template = [
    NetFlowTemplatev9Field(type_template=1, length= 4),
    NetFlowTemplatev9Field(type_template=2, length= 4),
    NetFlowTemplatev9Field(type_template=4, length= 1),
    NetFlowTemplatev9Field(type_template=5, length= 1),
    NetFlowTemplatev9Field(type_template=6, length= 1),
    NetFlowTemplatev9Field(type_template=7, length= 2),
    NetFlowTemplatev9Field(type_template=10, length= 2),
    NetFlowTemplatev9Field(type_template=11, length= 2),
    NetFlowTemplatev9Field(type_template=14, length= 2),
    NetFlowTemplatev9Field(type_template=16, length= 4),
    NetFlowTemplatev9Field(type_template=17, length= 4),
    NetFlowTemplatev9Field(type_template=21, length= 4),
    NetFlowTemplatev9Field(type_template=22, length= 4),
    NetFlowTemplatev9Field(type_template=27, length= 16),
    NetFlowTemplatev9Field(type_template=28, length= 16),
    NetFlowTemplatev9Field(type_template=29, length= 1),
    NetFlowTemplatev9Field(type_template=30, length= 1),
    NetFlowTemplatev9Field(type_template=62, length= 16)
    ]

flowSet_2_header = FlowSet_Header_v9(FlowSet_id= 258, FlowSet_length=92)


flows = [
    Flow_v9(\
        Packets=826, Protocol=17, IP_ToS=0x00, TCP_Flags=0x00, Octets=113162,\
        SrcPort=2416, InputInt=0, DstPort=53, OutputInt=0, SrcAS=0, DstAS=0,\
        StartTime=0.002000000, EndTime=27.061000000,\
        SrcAddr="3ffe:507:0:1:200:86ff:fe05:80da",\
        DstAddr="3ffe:501:4819::42", SrcMask=0, DstMask=0, NextHop="::", 
        Padding=3)
    ]



data = Ether()/IP()/UDP(sport=64114,dport=2055)
data/=header_v9/flowSet_header_v9/flowset_id_v9

for t in template:
    data/=t

data/=flowSet_2_header

for f in flows:
    data/=f


wrpcap('v9.pcap', data)
