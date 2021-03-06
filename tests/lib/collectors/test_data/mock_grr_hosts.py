"""Mocks objects and protos for the GRR Host module tests."""

from google.protobuf import text_format

from grr_response_proto.api import client_pb2
from grr_response_proto.api import flow_pb2
from grr_api_client import flow
from grr_api_client import client

client_proto1 = """
  urn: "aff4:/C.0000000000000000"
  os_info {
    system: "Linux"
    release: "debian"
    version: "buster/sid"
    machine: "x86_64"
    kernel: "4.9.0-3-amd64"
    fqdn: "tomchop"
    install_date: 1480414461000000
  }
  first_seen_at: 1480416002507491
  last_seen_at: 1511174989891418
  last_booted_at: 1507912328000000
  last_clock: 1511174989272124
  age: 1510710503319681
  client_id: "C.0000000000000000"
"""

# This has a more recent install_date and last_seen date than client_proto1
client_proto2 = """
  urn: "aff4:/C.0000000000000001"
  os_info {
    system: "Linux"
    release: "debian"
    version: "buster/sid"
    machine: "x86_64"
    kernel: "4.9.0-3-amd64"
    fqdn: "tomchop"
    install_date: 1480414461020000
  }
  first_seen_at: 1480416002507491
  last_seen_at: 1511174989892418
  last_booted_at: 1507912328000000
  last_clock: 1511174989272124
  age: 1510710503319681
  client_id: "C.0000000000000001"
"""

MOCK_CLIENT = client.Client(
    data=text_format.Parse(client_proto1, client_pb2.ApiClient()), context=True)
MOCK_CLIENT_RECENT = client.Client(
    data=text_format.Parse(client_proto2, client_pb2.ApiClient()), context=True)
MOCK_CLIENT_LIST = [
    MOCK_CLIENT,
    MOCK_CLIENT_RECENT
]

flow_pb = flow_pb2.ApiFlow(urn="C.0000000000000001", flow_id="F:12345")
MOCK_FLOW = flow.Flow(data=flow_pb, context=True)
