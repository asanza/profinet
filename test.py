

from pnio.util import ethernet_socket, get_mac
import pnio.dcp as dcp
import pnio.rpc as rpc

s = ethernet_socket("eth0", 3)
src = get_mac("eth0")

dcp.send_discover(s, src)
dcp.read_response(s, src,  once=True, debug=True)

info = rpc.get_station_info(s, src, "dut")

con = rpc.RPCCon(info)
con.connect(src)
r = con.release(src)
print(r.payload)
print(r)

# while(True):
#     iod = con.read(0, 1, 1, 0x43D, 8)
#     print(iod.payload)