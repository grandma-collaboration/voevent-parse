#!/usr/bin/env python3
"""Test VOEvent parsing with the SVOM example"""

import sys

# Try to import voeventparse
try:
    import voeventparse as vp

    print("✓ voeventparse imported successfully")
except ImportError as e:
    print(f"✗ Failed to import voeventparse: {e}")
    sys.exit(1)

# SVOM ECLAIRs example from user
svom_xml = b"""<?xml version='1.0' encoding='UTF-8'?>
<voe:VOEvent xmlns:voe="http://www.ivoa.net/xml/VOEvent/v2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.ivoa.net/xml/VOEvent/v2.0 http://www.ivoa.net/xml/VOEvent/VOEvent-v2.0.xsd" role="observation" version="2.0" ivorn="ivo://org.svom/fsc#sb25120806_eclairs-wakeup">
  <Who>
    <AuthorIVORN>ivo://org.svom/fsc</AuthorIVORN>
    <Date>2025-12-08T17:02:15+00:00</Date>
    <Author>
      <title>{"full_name": "SVOM French Science Center", "ref": "https://fsc.svom.org/readthedocs"}</title>
      <shortName>FSC</shortName>
      <contactName>Timothe Roland</contactName>
      <contactEmail>svom-contact@cea.fr</contactEmail>
    </Author>
  </Who>
  <What>
    <Param name="Packet_Type" value="202" ucd="meta.id"/>
    <Param name="Pkt_Ser_Num" value="1" ucd="meta.id"/>
    <Param name="Instrument" value="ECLAIRs" ucd="instr"/>
    <Group name="Svom_Identifiers">
      <Param name="Notice_Level" value="N1e" ucd="meta.id"/>
      <Param name="Burst_Id" value="sb25120806" ucd="meta.id"/>
    </Group>
  </What>
  <WhereWhen>
    <ObsDataLocation>
      <ObservatoryLocation id="GEOLEO"/>
      <ObservationLocation>
        <AstroCoordSystem id="UTC-ICRS-GEO"/>
        <AstroCoords coord_system_id="UTC-ICRS-GEO">
          <Time unit="s">
            <TimeInstant>
              <ISOTime>2025-12-08T16:50:21.314000</ISOTime>
            </TimeInstant>
          </Time>
          <Position2D unit="deg">
            <Name1>RA</Name1>
            <Name2>Dec</Name2>
            <Value2>
              <C1>337.5347</C1>
              <C2>-0.3918</C2>
            </Value2>
            <Error2Radius>0.1962</Error2Radius>
          </Position2D>
        </AstroCoords>
      </ObservationLocation>
    </ObsDataLocation>
  </WhereWhen>
  <How>
    <Description>N1e notice, data from ECLAIRs</Description>
    <Reference uri="https://www.svom.eu/en/telescope-eclairs-en/"/>
  </How>
</voe:VOEvent>
"""

print("\n" + "=" * 60)
print("Testing VOEvent parsing with SVOM example")
print("=" * 60)

try:
    # Parse the VOEvent
    voevent = vp.loads(svom_xml)
    print("✓ VOEvent parsed successfully")

    # Test ivorn extraction
    ivorn = voevent.attrib.get("ivorn", "")
    print(f"\nivorn: {ivorn}")

    # Test toplevel params
    print("\n--- Toplevel Parameters ---")
    top_params = vp.get_toplevel_params(voevent)
    for param_name, param_attribs in top_params.items():
        print(f"  {param_name}: {param_attribs['value']}")

    # Test grouped params
    print("\n--- Grouped Parameters ---")
    grouped_params = vp.get_grouped_params(voevent)
    for group_name, group_params in grouped_params.items():
        print(f"  Group: {group_name}")
        for param_name, param_attribs in group_params.items():
            print(f"    {param_name}: {param_attribs['value']}")

    # Test position extraction
    print("\n--- Position ---")
    position = vp.get_event_position(voevent)
    print(f"  RA: {position.ra:.4f} deg")
    print(f"  Dec: {position.dec:.4f} deg")
    print(f"  Error: {position.err:.4f} deg ({position.err * 60:.2f} arcmin)")
    print(f"  System: {position.system}")

    # Test time extraction
    print("\n--- Time ---")
    event_time = vp.get_event_time_as_utc(voevent)
    print(f"  Trigger time: {event_time}")
    print(f"  Formatted: {event_time.strftime('%Y-%m-%d %H:%M:%S UTC')}")

    # Test Burst_Id extraction (SVOM specific)
    print("\n--- SVOM Trigger ID ---")
    if "Svom_Identifiers" in grouped_params:
        burst_id = grouped_params["Svom_Identifiers"]["Burst_Id"]["value"]
        print(f"  Burst_Id: {burst_id}")

    print("\n✓ All tests passed!")

except Exception as e:
    print(f"\n✗ Error during parsing: {e}")
    import traceback

    traceback.print_exc()
    sys.exit(1)
