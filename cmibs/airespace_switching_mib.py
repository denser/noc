# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# AIRESPACE-SWITCHING-MIB
#     Compiled MIB
#     Do not modify this file directly
#     Run ./noc mib make_cmib instead
# ----------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# MIB Name
NAME = "AIRESPACE-SWITCHING-MIB"
# Metadata
LAST_UPDATED = "2006-04-10"
COMPILED = "2018-06-19"
# MIB Data: name -> oid
MIB = {
    "AIRESPACE-SWITCHING-MIB::bsnSwitching": "1.3.6.1.4.1.14179.1",
    "AIRESPACE-SWITCHING-MIB::agentInfoGroup": "1.3.6.1.4.1.14179.1.1",
    "AIRESPACE-SWITCHING-MIB::agentInventoryGroup": "1.3.6.1.4.1.14179.1.1.1",
    "AIRESPACE-SWITCHING-MIB::agentInventorySysDescription": "1.3.6.1.4.1.14179.1.1.1.1",
    "AIRESPACE-SWITCHING-MIB::agentInventoryMachineType": "1.3.6.1.4.1.14179.1.1.1.2",
    "AIRESPACE-SWITCHING-MIB::agentInventoryMachineModel": "1.3.6.1.4.1.14179.1.1.1.3",
    "AIRESPACE-SWITCHING-MIB::agentInventorySerialNumber": "1.3.6.1.4.1.14179.1.1.1.4",
    "AIRESPACE-SWITCHING-MIB::agentInventoryMaintenanceLevel": "1.3.6.1.4.1.14179.1.1.1.6",
    "AIRESPACE-SWITCHING-MIB::agentInventoryBurnedInMacAddress": "1.3.6.1.4.1.14179.1.1.1.9",
    "AIRESPACE-SWITCHING-MIB::agentInventoryOperatingSystem": "1.3.6.1.4.1.14179.1.1.1.10",
    "AIRESPACE-SWITCHING-MIB::agentInventoryManufacturerName": "1.3.6.1.4.1.14179.1.1.1.12",
    "AIRESPACE-SWITCHING-MIB::agentInventoryProductName": "1.3.6.1.4.1.14179.1.1.1.13",
    "AIRESPACE-SWITCHING-MIB::agentInventoryProductVersion": "1.3.6.1.4.1.14179.1.1.1.14",
    "AIRESPACE-SWITCHING-MIB::agentInventoryIsGigECardPresent": "1.3.6.1.4.1.14179.1.1.1.15",
    "AIRESPACE-SWITCHING-MIB::agentInventoryIsCryptoCardPresent": "1.3.6.1.4.1.14179.1.1.1.16",
    "AIRESPACE-SWITCHING-MIB::agentInventoryIsForeignAPSupported": "1.3.6.1.4.1.14179.1.1.1.17",
    "AIRESPACE-SWITCHING-MIB::agentInventoryMaxNumberOfAPsSupported": "1.3.6.1.4.1.14179.1.1.1.18",
    "AIRESPACE-SWITCHING-MIB::agentInventoryIsCryptoCard2Present": "1.3.6.1.4.1.14179.1.1.1.19",
    "AIRESPACE-SWITCHING-MIB::agentInventoryFipsModeEnabled": "1.3.6.1.4.1.14179.1.1.1.20",
    "AIRESPACE-SWITCHING-MIB::agentTrapLogGroup": "1.3.6.1.4.1.14179.1.1.2",
    "AIRESPACE-SWITCHING-MIB::agentTrapLogTotal": "1.3.6.1.4.1.14179.1.1.2.1",
    "AIRESPACE-SWITCHING-MIB::agentTrapLogTotalSinceLastViewed": "1.3.6.1.4.1.14179.1.1.2.3",
    "AIRESPACE-SWITCHING-MIB::agentTrapLogTable": "1.3.6.1.4.1.14179.1.1.2.4",
    "AIRESPACE-SWITCHING-MIB::agentTrapLogEntry": "1.3.6.1.4.1.14179.1.1.2.4.1",
    "AIRESPACE-SWITCHING-MIB::agentTrapLogIndex": "1.3.6.1.4.1.14179.1.1.2.4.1.1",
    "AIRESPACE-SWITCHING-MIB::agentTrapLogSystemTime": "1.3.6.1.4.1.14179.1.1.2.4.1.2",
    "AIRESPACE-SWITCHING-MIB::agentTrapLogTrap": "1.3.6.1.4.1.14179.1.1.2.4.1.22",
    "AIRESPACE-SWITCHING-MIB::agentRadioUpDownTrapCount": "1.3.6.1.4.1.14179.1.1.2.5",
    "AIRESPACE-SWITCHING-MIB::agentApAssociateDisassociateTrapCount": "1.3.6.1.4.1.14179.1.1.2.6",
    "AIRESPACE-SWITCHING-MIB::agentApLoadProfileFailTrapCount": "1.3.6.1.4.1.14179.1.1.2.7",
    "AIRESPACE-SWITCHING-MIB::agentApNoiseProfileFailTrapCount": "1.3.6.1.4.1.14179.1.1.2.8",
    "AIRESPACE-SWITCHING-MIB::agentApInterferenceProfileFailTrapCount": "1.3.6.1.4.1.14179.1.1.2.9",
    "AIRESPACE-SWITCHING-MIB::agentApCoverageProfileFailTrapCount": "1.3.6.1.4.1.14179.1.1.2.10",
    "AIRESPACE-SWITCHING-MIB::agentSwitchInfoGroup": "1.3.6.1.4.1.14179.1.1.3",
    "AIRESPACE-SWITCHING-MIB::agentSwitchInfoLwappTransportMode": "1.3.6.1.4.1.14179.1.1.3.1",
    "AIRESPACE-SWITCHING-MIB::agentSwitchInfoPowerSupply1Present": "1.3.6.1.4.1.14179.1.1.3.2",
    "AIRESPACE-SWITCHING-MIB::agentSwitchInfoPowerSupply1Operational": "1.3.6.1.4.1.14179.1.1.3.3",
    "AIRESPACE-SWITCHING-MIB::agentSwitchInfoPowerSupply2Present": "1.3.6.1.4.1.14179.1.1.3.4",
    "AIRESPACE-SWITCHING-MIB::agentSwitchInfoPowerSupply2Operational": "1.3.6.1.4.1.14179.1.1.3.5",
    "AIRESPACE-SWITCHING-MIB::agentProductGroup": "1.3.6.1.4.1.14179.1.1.4",
    "AIRESPACE-SWITCHING-MIB::productGroup1": "1.3.6.1.4.1.14179.1.1.4.1",
    "AIRESPACE-SWITCHING-MIB::productGroup2": "1.3.6.1.4.1.14179.1.1.4.2",
    "AIRESPACE-SWITCHING-MIB::productGroup3": "1.3.6.1.4.1.14179.1.1.4.3",
    "AIRESPACE-SWITCHING-MIB::productGroup4": "1.3.6.1.4.1.14179.1.1.4.4",
    "AIRESPACE-SWITCHING-MIB::agentResourceInfoGroup": "1.3.6.1.4.1.14179.1.1.5",
    "AIRESPACE-SWITCHING-MIB::agentCurrentCPUUtilization": "1.3.6.1.4.1.14179.1.1.5.1",
    "AIRESPACE-SWITCHING-MIB::agentTotalMemory": "1.3.6.1.4.1.14179.1.1.5.2",
    "AIRESPACE-SWITCHING-MIB::agentFreeMemory": "1.3.6.1.4.1.14179.1.1.5.3",
    "AIRESPACE-SWITCHING-MIB::agentWcpInfoGroup": "1.3.6.1.4.1.14179.1.1.6",
    "AIRESPACE-SWITCHING-MIB::agentWcpDeviceName": "1.3.6.1.4.1.14179.1.1.6.1",
    "AIRESPACE-SWITCHING-MIB::agentWcpSlotNumber": "1.3.6.1.4.1.14179.1.1.6.2",
    "AIRESPACE-SWITCHING-MIB::agentWcpPortNumber": "1.3.6.1.4.1.14179.1.1.6.3",
    "AIRESPACE-SWITCHING-MIB::agentWcpPeerPortNumber": "1.3.6.1.4.1.14179.1.1.6.4",
    "AIRESPACE-SWITCHING-MIB::agentWcpPeerIpAddress": "1.3.6.1.4.1.14179.1.1.6.5",
    "AIRESPACE-SWITCHING-MIB::agentWcpControllerTableChecksum": "1.3.6.1.4.1.14179.1.1.6.6",
    "AIRESPACE-SWITCHING-MIB::agentWcpControllerInfoTable": "1.3.6.1.4.1.14179.1.1.6.7",
    "AIRESPACE-SWITCHING-MIB::agentWcpControllerInfoEntry": "1.3.6.1.4.1.14179.1.1.6.7.1",
    "AIRESPACE-SWITCHING-MIB::agentWcpControllerInfoSlotNumber": "1.3.6.1.4.1.14179.1.1.6.7.1.1",
    "AIRESPACE-SWITCHING-MIB::agentWcpControllerInfoPortNumber": "1.3.6.1.4.1.14179.1.1.6.7.1.2",
    "AIRESPACE-SWITCHING-MIB::agentWcpControllerInfoIpAddress": "1.3.6.1.4.1.14179.1.1.6.7.1.10",
    "AIRESPACE-SWITCHING-MIB::agentConfigGroup": "1.3.6.1.4.1.14179.1.2",
    "AIRESPACE-SWITCHING-MIB::agentCLIConfigGroup": "1.3.6.1.4.1.14179.1.2.1",
    "AIRESPACE-SWITCHING-MIB::agentLoginSessionTable": "1.3.6.1.4.1.14179.1.2.1.1",
    "AIRESPACE-SWITCHING-MIB::agentLoginSessionEntry": "1.3.6.1.4.1.14179.1.2.1.1.1",
    "AIRESPACE-SWITCHING-MIB::agentLoginSessionIndex": "1.3.6.1.4.1.14179.1.2.1.1.1.1",
    "AIRESPACE-SWITCHING-MIB::agentLoginSessionUserName": "1.3.6.1.4.1.14179.1.2.1.1.1.2",
    "AIRESPACE-SWITCHING-MIB::agentLoginSessionIPAddress": "1.3.6.1.4.1.14179.1.2.1.1.1.3",
    "AIRESPACE-SWITCHING-MIB::agentLoginSessionConnectionType": "1.3.6.1.4.1.14179.1.2.1.1.1.4",
    "AIRESPACE-SWITCHING-MIB::agentLoginSessionIdleTime": "1.3.6.1.4.1.14179.1.2.1.1.1.5",
    "AIRESPACE-SWITCHING-MIB::agentLoginSessionSessionTime": "1.3.6.1.4.1.14179.1.2.1.1.1.6",
    "AIRESPACE-SWITCHING-MIB::agentLoginSessionStatus": "1.3.6.1.4.1.14179.1.2.1.1.1.26",
    "AIRESPACE-SWITCHING-MIB::agentTelnetConfigGroup": "1.3.6.1.4.1.14179.1.2.1.2",
    "AIRESPACE-SWITCHING-MIB::agentTelnetLoginTimeout": "1.3.6.1.4.1.14179.1.2.1.2.1",
    "AIRESPACE-SWITCHING-MIB::agentTelnetMaxSessions": "1.3.6.1.4.1.14179.1.2.1.2.2",
    "AIRESPACE-SWITCHING-MIB::agentTelnetAllowNewMode": "1.3.6.1.4.1.14179.1.2.1.2.3",
    "AIRESPACE-SWITCHING-MIB::agentSSHAllowNewMode": "1.3.6.1.4.1.14179.1.2.1.2.4",
    "AIRESPACE-SWITCHING-MIB::agentSerialGroup": "1.3.6.1.4.1.14179.1.2.1.5",
    "AIRESPACE-SWITCHING-MIB::agentSerialTimeout": "1.3.6.1.4.1.14179.1.2.1.5.1",
    "AIRESPACE-SWITCHING-MIB::agentSerialBaudrate": "1.3.6.1.4.1.14179.1.2.1.5.2",
    "AIRESPACE-SWITCHING-MIB::agentSerialCharacterSize": "1.3.6.1.4.1.14179.1.2.1.5.3",
    "AIRESPACE-SWITCHING-MIB::agentSerialHWFlowControlMode": "1.3.6.1.4.1.14179.1.2.1.5.4",
    "AIRESPACE-SWITCHING-MIB::agentSerialStopBits": "1.3.6.1.4.1.14179.1.2.1.5.5",
    "AIRESPACE-SWITCHING-MIB::agentSerialParityType": "1.3.6.1.4.1.14179.1.2.1.5.6",
    "AIRESPACE-SWITCHING-MIB::agentLagConfigGroup": "1.3.6.1.4.1.14179.1.2.2",
    "AIRESPACE-SWITCHING-MIB::agentLagConfigCreate": "1.3.6.1.4.1.14179.1.2.2.1",
    "AIRESPACE-SWITCHING-MIB::agentLagSummaryConfigTable": "1.3.6.1.4.1.14179.1.2.2.2",
    "AIRESPACE-SWITCHING-MIB::agentLagSummaryConfigEntry": "1.3.6.1.4.1.14179.1.2.2.2.1",
    "AIRESPACE-SWITCHING-MIB::agentLagSummaryName": "1.3.6.1.4.1.14179.1.2.2.2.1.1",
    "AIRESPACE-SWITCHING-MIB::agentLagSummaryLagIndex": "1.3.6.1.4.1.14179.1.2.2.2.1.2",
    "AIRESPACE-SWITCHING-MIB::agentLagSummaryFlushTimer": "1.3.6.1.4.1.14179.1.2.2.2.1.3",
    "AIRESPACE-SWITCHING-MIB::agentLagSummaryLinkTrap": "1.3.6.1.4.1.14179.1.2.2.2.1.4",
    "AIRESPACE-SWITCHING-MIB::agentLagSummaryAdminMode": "1.3.6.1.4.1.14179.1.2.2.2.1.5",
    "AIRESPACE-SWITCHING-MIB::agentLagSummaryStpMode": "1.3.6.1.4.1.14179.1.2.2.2.1.6",
    "AIRESPACE-SWITCHING-MIB::agentLagSummaryAddPort": "1.3.6.1.4.1.14179.1.2.2.2.1.7",
    "AIRESPACE-SWITCHING-MIB::agentLagSummaryDeletePort": "1.3.6.1.4.1.14179.1.2.2.2.1.8",
    "AIRESPACE-SWITCHING-MIB::agentLagSummaryPortsBitMask": "1.3.6.1.4.1.14179.1.2.2.2.1.9",
    "AIRESPACE-SWITCHING-MIB::agentLagSummaryStatus": "1.3.6.1.4.1.14179.1.2.2.2.1.30",
    "AIRESPACE-SWITCHING-MIB::agentLagDetailedConfigTable": "1.3.6.1.4.1.14179.1.2.2.3",
    "AIRESPACE-SWITCHING-MIB::agentLagDetailedConfigEntry": "1.3.6.1.4.1.14179.1.2.2.3.1",
    "AIRESPACE-SWITCHING-MIB::agentLagDetailedLagIndex": "1.3.6.1.4.1.14179.1.2.2.3.1.1",
    "AIRESPACE-SWITCHING-MIB::agentLagDetailedIfIndex": "1.3.6.1.4.1.14179.1.2.2.3.1.2",
    "AIRESPACE-SWITCHING-MIB::agentLagDetailedPortSpeed": "1.3.6.1.4.1.14179.1.2.2.3.1.22",
    "AIRESPACE-SWITCHING-MIB::agentLagConfigMode": "1.3.6.1.4.1.14179.1.2.2.4",
    "AIRESPACE-SWITCHING-MIB::agentNetworkConfigGroup": "1.3.6.1.4.1.14179.1.2.3",
    "AIRESPACE-SWITCHING-MIB::agentNetworkIPAddress": "1.3.6.1.4.1.14179.1.2.3.1",
    "AIRESPACE-SWITCHING-MIB::agentNetworkSubnetMask": "1.3.6.1.4.1.14179.1.2.3.2",
    "AIRESPACE-SWITCHING-MIB::agentNetworkDefaultGateway": "1.3.6.1.4.1.14179.1.2.3.3",
    "AIRESPACE-SWITCHING-MIB::agentNetworkBurnedInMacAddress": "1.3.6.1.4.1.14179.1.2.3.4",
    "AIRESPACE-SWITCHING-MIB::agentNetworkConfigProtocol": "1.3.6.1.4.1.14179.1.2.3.7",
    "AIRESPACE-SWITCHING-MIB::agentNetworkWebMode": "1.3.6.1.4.1.14179.1.2.3.8",
    "AIRESPACE-SWITCHING-MIB::agentNetworkSecureWebMode": "1.3.6.1.4.1.14179.1.2.3.9",
    "AIRESPACE-SWITCHING-MIB::agentNetworkMulticastMode": "1.3.6.1.4.1.14179.1.2.3.10",
    "AIRESPACE-SWITCHING-MIB::agentNetworkDsPortNumber": "1.3.6.1.4.1.14179.1.2.3.11",
    "AIRESPACE-SWITCHING-MIB::agentNetworkUserIdleTimeout": "1.3.6.1.4.1.14179.1.2.3.12",
    "AIRESPACE-SWITCHING-MIB::agentNetworkArpTimeout": "1.3.6.1.4.1.14179.1.2.3.13",
    "AIRESPACE-SWITCHING-MIB::agentNetworkManagementVlan": "1.3.6.1.4.1.14179.1.2.3.14",
    "AIRESPACE-SWITCHING-MIB::agentNetworkGvrpStatus": "1.3.6.1.4.1.14179.1.2.3.15",
    "AIRESPACE-SWITCHING-MIB::agentNetworkAllowMgmtViaWireless": "1.3.6.1.4.1.14179.1.2.3.16",
    "AIRESPACE-SWITCHING-MIB::agentNetworkBroadcastSsidMode": "1.3.6.1.4.1.14179.1.2.3.17",
    "AIRESPACE-SWITCHING-MIB::agentNetworkSecureWebPassword": "1.3.6.1.4.1.14179.1.2.3.18",
    "AIRESPACE-SWITCHING-MIB::agentNetworkWebAdminCertType": "1.3.6.1.4.1.14179.1.2.3.19",
    "AIRESPACE-SWITCHING-MIB::agentNetworkWebAdminCertRegenerateCmdInvoke": "1.3.6.1.4.1.14179.1.2.3.20",
    "AIRESPACE-SWITCHING-MIB::agentNetworkWebAuthCertType": "1.3.6.1.4.1.14179.1.2.3.21",
    "AIRESPACE-SWITCHING-MIB::agentNetworkWebAuthCertRegenerateCmdInvoke": "1.3.6.1.4.1.14179.1.2.3.22",
    "AIRESPACE-SWITCHING-MIB::agentNetworkRouteConfigTable": "1.3.6.1.4.1.14179.1.2.3.23",
    "AIRESPACE-SWITCHING-MIB::agentNetworkRouteConfigEntry": "1.3.6.1.4.1.14179.1.2.3.23.1",
    "AIRESPACE-SWITCHING-MIB::agentNetworkRouteIPAddress": "1.3.6.1.4.1.14179.1.2.3.23.1.1",
    "AIRESPACE-SWITCHING-MIB::agentNetworkRouteIPNetmask": "1.3.6.1.4.1.14179.1.2.3.23.1.2",
    "AIRESPACE-SWITCHING-MIB::agentNetworkRouteGateway": "1.3.6.1.4.1.14179.1.2.3.23.1.3",
    "AIRESPACE-SWITCHING-MIB::agentNetworkRouteStatus": "1.3.6.1.4.1.14179.1.2.3.23.1.23",
    "AIRESPACE-SWITCHING-MIB::agentNetworkPeerToPeerBlockingMode": "1.3.6.1.4.1.14179.1.2.3.24",
    "AIRESPACE-SWITCHING-MIB::agentNetworkMulticastGroupAddress": "1.3.6.1.4.1.14179.1.2.3.25",
    "AIRESPACE-SWITCHING-MIB::agentServicePortConfigGroup": "1.3.6.1.4.1.14179.1.2.4",
    "AIRESPACE-SWITCHING-MIB::agentServicePortIPAddress": "1.3.6.1.4.1.14179.1.2.4.1",
    "AIRESPACE-SWITCHING-MIB::agentServicePortSubnetMask": "1.3.6.1.4.1.14179.1.2.4.2",
    "AIRESPACE-SWITCHING-MIB::agentServicePortDefaultGateway": "1.3.6.1.4.1.14179.1.2.4.3",
    "AIRESPACE-SWITCHING-MIB::agentServicePortBurnedInMacAddress": "1.3.6.1.4.1.14179.1.2.4.4",
    "AIRESPACE-SWITCHING-MIB::agentServicePortConfigProtocol": "1.3.6.1.4.1.14179.1.2.4.5",
    "AIRESPACE-SWITCHING-MIB::agentSnmpConfigGroup": "1.3.6.1.4.1.14179.1.2.5",
    "AIRESPACE-SWITCHING-MIB::agentSnmpTrapPortNumber": "1.3.6.1.4.1.14179.1.2.5.1",
    "AIRESPACE-SWITCHING-MIB::agentSnmpVersion1Status": "1.3.6.1.4.1.14179.1.2.5.2",
    "AIRESPACE-SWITCHING-MIB::agentSnmpVersion2cStatus": "1.3.6.1.4.1.14179.1.2.5.3",
    "AIRESPACE-SWITCHING-MIB::agentSnmpCommunityConfigTable": "1.3.6.1.4.1.14179.1.2.5.5",
    "AIRESPACE-SWITCHING-MIB::agentSnmpCommunityConfigEntry": "1.3.6.1.4.1.14179.1.2.5.5.1",
    "AIRESPACE-SWITCHING-MIB::agentSnmpCommunityName": "1.3.6.1.4.1.14179.1.2.5.5.1.1",
    "AIRESPACE-SWITCHING-MIB::agentSnmpCommunityIPAddress": "1.3.6.1.4.1.14179.1.2.5.5.1.2",
    "AIRESPACE-SWITCHING-MIB::agentSnmpCommunityIPMask": "1.3.6.1.4.1.14179.1.2.5.5.1.3",
    "AIRESPACE-SWITCHING-MIB::agentSnmpCommunityAccessMode": "1.3.6.1.4.1.14179.1.2.5.5.1.4",
    "AIRESPACE-SWITCHING-MIB::agentSnmpCommunityEnabled": "1.3.6.1.4.1.14179.1.2.5.5.1.5",
    "AIRESPACE-SWITCHING-MIB::agentSnmpCommunityStatus": "1.3.6.1.4.1.14179.1.2.5.5.1.25",
    "AIRESPACE-SWITCHING-MIB::agentSnmpTrapReceiverConfigTable": "1.3.6.1.4.1.14179.1.2.5.6",
    "AIRESPACE-SWITCHING-MIB::agentSnmpTrapReceiverConfigEntry": "1.3.6.1.4.1.14179.1.2.5.6.1",
    "AIRESPACE-SWITCHING-MIB::agentSnmpTrapReceiverName": "1.3.6.1.4.1.14179.1.2.5.6.1.1",
    "AIRESPACE-SWITCHING-MIB::agentSnmpTrapReceiverIPAddress": "1.3.6.1.4.1.14179.1.2.5.6.1.2",
    "AIRESPACE-SWITCHING-MIB::agentSnmpTrapReceiverEnabled": "1.3.6.1.4.1.14179.1.2.5.6.1.3",
    "AIRESPACE-SWITCHING-MIB::agentSnmpTrapReceiverStatus": "1.3.6.1.4.1.14179.1.2.5.6.1.23",
    "AIRESPACE-SWITCHING-MIB::agentSnmpTrapFlagsConfigGroup": "1.3.6.1.4.1.14179.1.2.5.7",
    "AIRESPACE-SWITCHING-MIB::agentSnmpAuthenticationTrapFlag": "1.3.6.1.4.1.14179.1.2.5.7.1",
    "AIRESPACE-SWITCHING-MIB::agentSnmpLinkUpDownTrapFlag": "1.3.6.1.4.1.14179.1.2.5.7.2",
    "AIRESPACE-SWITCHING-MIB::agentSnmpMultipleUsersTrapFlag": "1.3.6.1.4.1.14179.1.2.5.7.3",
    "AIRESPACE-SWITCHING-MIB::agentSnmpSpanningTreeTrapFlag": "1.3.6.1.4.1.14179.1.2.5.7.4",
    "AIRESPACE-SWITCHING-MIB::agentSnmpBroadcastStormTrapFlag": "1.3.6.1.4.1.14179.1.2.5.7.5",
    "AIRESPACE-SWITCHING-MIB::agentSnmpV3ConfigGroup": "1.3.6.1.4.1.14179.1.2.6",
    "AIRESPACE-SWITCHING-MIB::agentSnmpVersion3Status": "1.3.6.1.4.1.14179.1.2.6.1",
    "AIRESPACE-SWITCHING-MIB::agentSnmpV3UserConfigTable": "1.3.6.1.4.1.14179.1.2.6.2",
    "AIRESPACE-SWITCHING-MIB::agentSnmpV3UserConfigEntry": "1.3.6.1.4.1.14179.1.2.6.2.1",
    "AIRESPACE-SWITCHING-MIB::agentSnmpV3UserName": "1.3.6.1.4.1.14179.1.2.6.2.1.1",
    "AIRESPACE-SWITCHING-MIB::agentSnmpV3UserAccessMode": "1.3.6.1.4.1.14179.1.2.6.2.1.2",
    "AIRESPACE-SWITCHING-MIB::agentSnmpV3UserAuthenticationType": "1.3.6.1.4.1.14179.1.2.6.2.1.3",
    "AIRESPACE-SWITCHING-MIB::agentSnmpV3UserEncryptionType": "1.3.6.1.4.1.14179.1.2.6.2.1.4",
    "AIRESPACE-SWITCHING-MIB::agentSnmpV3UserAuthenticationPassword": "1.3.6.1.4.1.14179.1.2.6.2.1.5",
    "AIRESPACE-SWITCHING-MIB::agentSnmpV3UserEncryptionPassword": "1.3.6.1.4.1.14179.1.2.6.2.1.6",
    "AIRESPACE-SWITCHING-MIB::agentSnmpV3UserStatus": "1.3.6.1.4.1.14179.1.2.6.2.1.26",
    "AIRESPACE-SWITCHING-MIB::agentSpanningTreeConfigGroup": "1.3.6.1.4.1.14179.1.2.7",
    "AIRESPACE-SWITCHING-MIB::agentSpanningTreeMode": "1.3.6.1.4.1.14179.1.2.7.1",
    "AIRESPACE-SWITCHING-MIB::agentSwitchConfigGroup": "1.3.6.1.4.1.14179.1.2.8",
    "AIRESPACE-SWITCHING-MIB::agentSwitchBroadcastControlMode": "1.3.6.1.4.1.14179.1.2.8.2",
    "AIRESPACE-SWITCHING-MIB::agentSwitchDot3FlowControlMode": "1.3.6.1.4.1.14179.1.2.8.3",
    "AIRESPACE-SWITCHING-MIB::agentSwitchAddressAgingTimeoutTable": "1.3.6.1.4.1.14179.1.2.8.4",
    "AIRESPACE-SWITCHING-MIB::agentSwitchAddressAgingTimeoutEntry": "1.3.6.1.4.1.14179.1.2.8.4.1",
    "AIRESPACE-SWITCHING-MIB::agentSwitchAddressAgingTimeout": "1.3.6.1.4.1.14179.1.2.8.4.1.10",
    "AIRESPACE-SWITCHING-MIB::agentSwitchLwappTransportMode": "1.3.6.1.4.1.14179.1.2.8.5",
    "AIRESPACE-SWITCHING-MIB::agentTransferConfigGroup": "1.3.6.1.4.1.14179.1.2.9",
    "AIRESPACE-SWITCHING-MIB::agentTransferUploadGroup": "1.3.6.1.4.1.14179.1.2.9.1",
    "AIRESPACE-SWITCHING-MIB::agentTransferUploadMode": "1.3.6.1.4.1.14179.1.2.9.1.1",
    "AIRESPACE-SWITCHING-MIB::agentTransferUploadServerIP": "1.3.6.1.4.1.14179.1.2.9.1.2",
    "AIRESPACE-SWITCHING-MIB::agentTransferUploadPath": "1.3.6.1.4.1.14179.1.2.9.1.3",
    "AIRESPACE-SWITCHING-MIB::agentTransferUploadFilename": "1.3.6.1.4.1.14179.1.2.9.1.4",
    "AIRESPACE-SWITCHING-MIB::agentTransferUploadDataType": "1.3.6.1.4.1.14179.1.2.9.1.5",
    "AIRESPACE-SWITCHING-MIB::agentTransferUploadStart": "1.3.6.1.4.1.14179.1.2.9.1.6",
    "AIRESPACE-SWITCHING-MIB::agentTransferUploadStatus": "1.3.6.1.4.1.14179.1.2.9.1.7",
    "AIRESPACE-SWITCHING-MIB::agentTransferDownloadGroup": "1.3.6.1.4.1.14179.1.2.9.2",
    "AIRESPACE-SWITCHING-MIB::agentTransferDownloadMode": "1.3.6.1.4.1.14179.1.2.9.2.1",
    "AIRESPACE-SWITCHING-MIB::agentTransferDownloadServerIP": "1.3.6.1.4.1.14179.1.2.9.2.2",
    "AIRESPACE-SWITCHING-MIB::agentTransferDownloadPath": "1.3.6.1.4.1.14179.1.2.9.2.3",
    "AIRESPACE-SWITCHING-MIB::agentTransferDownloadFilename": "1.3.6.1.4.1.14179.1.2.9.2.4",
    "AIRESPACE-SWITCHING-MIB::agentTransferDownloadDataType": "1.3.6.1.4.1.14179.1.2.9.2.5",
    "AIRESPACE-SWITCHING-MIB::agentTransferDownloadStart": "1.3.6.1.4.1.14179.1.2.9.2.6",
    "AIRESPACE-SWITCHING-MIB::agentTransferDownloadStatus": "1.3.6.1.4.1.14179.1.2.9.2.7",
    "AIRESPACE-SWITCHING-MIB::agentTransferDownloadTftpMaxRetries": "1.3.6.1.4.1.14179.1.2.9.2.8",
    "AIRESPACE-SWITCHING-MIB::agentTransferDownloadTftpTimeout": "1.3.6.1.4.1.14179.1.2.9.2.9",
    "AIRESPACE-SWITCHING-MIB::agentTransferConfigurationFileEncryption": "1.3.6.1.4.1.14179.1.2.9.3",
    "AIRESPACE-SWITCHING-MIB::agentTransferConfigurationFileEncryptionKey": "1.3.6.1.4.1.14179.1.2.9.4",
    "AIRESPACE-SWITCHING-MIB::agentDot3adAggPortTable": "1.3.6.1.4.1.14179.1.2.11",
    "AIRESPACE-SWITCHING-MIB::agentDot3adAggPortEntry": "1.3.6.1.4.1.14179.1.2.11.1",
    "AIRESPACE-SWITCHING-MIB::agentDot3adAggPort": "1.3.6.1.4.1.14179.1.2.11.1.1",
    "AIRESPACE-SWITCHING-MIB::agentDot3adAggPortLACPMode": "1.3.6.1.4.1.14179.1.2.11.1.21",
    "AIRESPACE-SWITCHING-MIB::agentPortConfigTable": "1.3.6.1.4.1.14179.1.2.12",
    "AIRESPACE-SWITCHING-MIB::agentPortConfigEntry": "1.3.6.1.4.1.14179.1.2.12.1",
    "AIRESPACE-SWITCHING-MIB::agentPortDot1dBasePort": "1.3.6.1.4.1.14179.1.2.12.1.1",
    "AIRESPACE-SWITCHING-MIB::agentPortIfIndex": "1.3.6.1.4.1.14179.1.2.12.1.2",
    "AIRESPACE-SWITCHING-MIB::agentPortIanaType": "1.3.6.1.4.1.14179.1.2.12.1.3",
    "AIRESPACE-SWITCHING-MIB::agentPortSTPMode": "1.3.6.1.4.1.14179.1.2.12.1.4",
    "AIRESPACE-SWITCHING-MIB::agentPortSTPState": "1.3.6.1.4.1.14179.1.2.12.1.5",
    "AIRESPACE-SWITCHING-MIB::agentPortAdminMode": "1.3.6.1.4.1.14179.1.2.12.1.6",
    "AIRESPACE-SWITCHING-MIB::agentPortPhysicalMode": "1.3.6.1.4.1.14179.1.2.12.1.7",
    "AIRESPACE-SWITCHING-MIB::agentPortPhysicalStatus": "1.3.6.1.4.1.14179.1.2.12.1.8",
    "AIRESPACE-SWITCHING-MIB::agentPortLinkTrapMode": "1.3.6.1.4.1.14179.1.2.12.1.9",
    "AIRESPACE-SWITCHING-MIB::agentPortClearStats": "1.3.6.1.4.1.14179.1.2.12.1.10",
    "AIRESPACE-SWITCHING-MIB::agentPortDefaultType": "1.3.6.1.4.1.14179.1.2.12.1.11",
    "AIRESPACE-SWITCHING-MIB::agentPortType": "1.3.6.1.4.1.14179.1.2.12.1.12",
    "AIRESPACE-SWITCHING-MIB::agentPortAutoNegAdminStatus": "1.3.6.1.4.1.14179.1.2.12.1.13",
    "AIRESPACE-SWITCHING-MIB::agentPortDot3FlowControlMode": "1.3.6.1.4.1.14179.1.2.12.1.14",
    "AIRESPACE-SWITCHING-MIB::agentPortPowerMode": "1.3.6.1.4.1.14179.1.2.12.1.15",
    "AIRESPACE-SWITCHING-MIB::agentPortGvrpStatus": "1.3.6.1.4.1.14179.1.2.12.1.16",
    "AIRESPACE-SWITCHING-MIB::agentPortGarpJoinTime": "1.3.6.1.4.1.14179.1.2.12.1.17",
    "AIRESPACE-SWITCHING-MIB::agentPortGarpLeaveTime": "1.3.6.1.4.1.14179.1.2.12.1.18",
    "AIRESPACE-SWITCHING-MIB::agentPortGarpLeaveAllTime": "1.3.6.1.4.1.14179.1.2.12.1.19",
    "AIRESPACE-SWITCHING-MIB::agentPortMirrorMode": "1.3.6.1.4.1.14179.1.2.12.1.20",
    "AIRESPACE-SWITCHING-MIB::agentPortMulticastApplianceMode": "1.3.6.1.4.1.14179.1.2.12.1.21",
    "AIRESPACE-SWITCHING-MIB::agentPortOperationalStatus": "1.3.6.1.4.1.14179.1.2.12.1.40",
    "AIRESPACE-SWITCHING-MIB::agentInterfaceConfigTable": "1.3.6.1.4.1.14179.1.2.13",
    "AIRESPACE-SWITCHING-MIB::agentInterfaceConfigEntry": "1.3.6.1.4.1.14179.1.2.13.1",
    "AIRESPACE-SWITCHING-MIB::agentInterfaceName": "1.3.6.1.4.1.14179.1.2.13.1.1",
    "AIRESPACE-SWITCHING-MIB::agentInterfaceVlanId": "1.3.6.1.4.1.14179.1.2.13.1.2",
    "AIRESPACE-SWITCHING-MIB::agentInterfaceType": "1.3.6.1.4.1.14179.1.2.13.1.3",
    "AIRESPACE-SWITCHING-MIB::agentInterfaceMacAddress": "1.3.6.1.4.1.14179.1.2.13.1.4",
    "AIRESPACE-SWITCHING-MIB::agentInterfaceIPAddress": "1.3.6.1.4.1.14179.1.2.13.1.5",
    "AIRESPACE-SWITCHING-MIB::agentInterfaceIPNetmask": "1.3.6.1.4.1.14179.1.2.13.1.6",
    "AIRESPACE-SWITCHING-MIB::agentInterfaceIPGateway": "1.3.6.1.4.1.14179.1.2.13.1.7",
    "AIRESPACE-SWITCHING-MIB::agentInterfacePortNo": "1.3.6.1.4.1.14179.1.2.13.1.8",
    "AIRESPACE-SWITCHING-MIB::agentInterfacePrimaryDhcpAddress": "1.3.6.1.4.1.14179.1.2.13.1.9",
    "AIRESPACE-SWITCHING-MIB::agentInterfaceSecondaryDhcpAddress": "1.3.6.1.4.1.14179.1.2.13.1.10",
    "AIRESPACE-SWITCHING-MIB::agentInterfaceDhcpProtocol": "1.3.6.1.4.1.14179.1.2.13.1.11",
    "AIRESPACE-SWITCHING-MIB::agentInterfaceDnsHostName": "1.3.6.1.4.1.14179.1.2.13.1.12",
    "AIRESPACE-SWITCHING-MIB::agentInterfaceAclName": "1.3.6.1.4.1.14179.1.2.13.1.13",
    "AIRESPACE-SWITCHING-MIB::agentInterfaceAPManagementFeature": "1.3.6.1.4.1.14179.1.2.13.1.14",
    "AIRESPACE-SWITCHING-MIB::agentInterfaceActivePortNo": "1.3.6.1.4.1.14179.1.2.13.1.15",
    "AIRESPACE-SWITCHING-MIB::agentInterfaceBackupPortNo": "1.3.6.1.4.1.14179.1.2.13.1.16",
    "AIRESPACE-SWITCHING-MIB::agentInterfaceVlanQuarantine": "1.3.6.1.4.1.14179.1.2.13.1.17",
    "AIRESPACE-SWITCHING-MIB::agentInterfaceRowStatus": "1.3.6.1.4.1.14179.1.2.13.1.31",
    "AIRESPACE-SWITCHING-MIB::agentNtpConfigGroup": "1.3.6.1.4.1.14179.1.2.14",
    "AIRESPACE-SWITCHING-MIB::agentNtpPollingInterval": "1.3.6.1.4.1.14179.1.2.14.1",
    "AIRESPACE-SWITCHING-MIB::agentNtpServerTable": "1.3.6.1.4.1.14179.1.2.14.2",
    "AIRESPACE-SWITCHING-MIB::agentNtpServerEntry": "1.3.6.1.4.1.14179.1.2.14.2.1",
    "AIRESPACE-SWITCHING-MIB::agentNtpServerIndex": "1.3.6.1.4.1.14179.1.2.14.2.1.1",
    "AIRESPACE-SWITCHING-MIB::agentNtpServerAddress": "1.3.6.1.4.1.14179.1.2.14.2.1.2",
    "AIRESPACE-SWITCHING-MIB::agentNtpServerRowStatus": "1.3.6.1.4.1.14179.1.2.14.2.1.20",
    "AIRESPACE-SWITCHING-MIB::agentDhcpConfigGroup": "1.3.6.1.4.1.14179.1.2.15",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeTable": "1.3.6.1.4.1.14179.1.2.15.1",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeEntry": "1.3.6.1.4.1.14179.1.2.15.1.1",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeIndex": "1.3.6.1.4.1.14179.1.2.15.1.1.1",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeName": "1.3.6.1.4.1.14179.1.2.15.1.1.2",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeLeaseTime": "1.3.6.1.4.1.14179.1.2.15.1.1.3",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeNetwork": "1.3.6.1.4.1.14179.1.2.15.1.1.4",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeNetmask": "1.3.6.1.4.1.14179.1.2.15.1.1.5",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopePoolStartAddress": "1.3.6.1.4.1.14179.1.2.15.1.1.6",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopePoolEndAddress": "1.3.6.1.4.1.14179.1.2.15.1.1.7",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeDefaultRouterAddress1": "1.3.6.1.4.1.14179.1.2.15.1.1.8",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeDefaultRouterAddress2": "1.3.6.1.4.1.14179.1.2.15.1.1.9",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeDefaultRouterAddress3": "1.3.6.1.4.1.14179.1.2.15.1.1.10",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeDnsDomainName": "1.3.6.1.4.1.14179.1.2.15.1.1.11",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeDnsServerAddress1": "1.3.6.1.4.1.14179.1.2.15.1.1.12",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeDnsServerAddress2": "1.3.6.1.4.1.14179.1.2.15.1.1.13",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeDnsServerAddress3": "1.3.6.1.4.1.14179.1.2.15.1.1.14",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeNetbiosNameServerAddress1": "1.3.6.1.4.1.14179.1.2.15.1.1.15",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeNetbiosNameServerAddress2": "1.3.6.1.4.1.14179.1.2.15.1.1.16",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeNetbiosNameServerAddress3": "1.3.6.1.4.1.14179.1.2.15.1.1.17",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeState": "1.3.6.1.4.1.14179.1.2.15.1.1.18",
    "AIRESPACE-SWITCHING-MIB::agentDhcpScopeRowStatus": "1.3.6.1.4.1.14179.1.2.15.1.1.30",
    "AIRESPACE-SWITCHING-MIB::agentSystemGroup": "1.3.6.1.4.1.14179.1.3",
    "AIRESPACE-SWITCHING-MIB::agentSaveConfig": "1.3.6.1.4.1.14179.1.3.1",
    "AIRESPACE-SWITCHING-MIB::agentClearConfig": "1.3.6.1.4.1.14179.1.3.2",
    "AIRESPACE-SWITCHING-MIB::agentClearLags": "1.3.6.1.4.1.14179.1.3.3",
    "AIRESPACE-SWITCHING-MIB::agentClearLoginSessions": "1.3.6.1.4.1.14179.1.3.4",
    "AIRESPACE-SWITCHING-MIB::agentClearPortStats": "1.3.6.1.4.1.14179.1.3.6",
    "AIRESPACE-SWITCHING-MIB::agentClearSwitchStats": "1.3.6.1.4.1.14179.1.3.7",
    "AIRESPACE-SWITCHING-MIB::agentClearTrapLog": "1.3.6.1.4.1.14179.1.3.8",
    "AIRESPACE-SWITCHING-MIB::agentResetSystem": "1.3.6.1.4.1.14179.1.3.10",
    "AIRESPACE-SWITCHING-MIB::stats": "1.3.6.1.4.1.14179.1.4",
    "AIRESPACE-SWITCHING-MIB::portStatsTable": "1.3.6.1.4.1.14179.1.4.1",
    "AIRESPACE-SWITCHING-MIB::portStatsEntry": "1.3.6.1.4.1.14179.1.4.1.1",
    "AIRESPACE-SWITCHING-MIB::portStatsIndex": "1.3.6.1.4.1.14179.1.4.1.1.1",
    "AIRESPACE-SWITCHING-MIB::portStatsPktsTx64Octets": "1.3.6.1.4.1.14179.1.4.1.1.2",
    "AIRESPACE-SWITCHING-MIB::portStatsPktsTx65to127Octets": "1.3.6.1.4.1.14179.1.4.1.1.3",
    "AIRESPACE-SWITCHING-MIB::portStatsPktsTx128to255Octets": "1.3.6.1.4.1.14179.1.4.1.1.4",
    "AIRESPACE-SWITCHING-MIB::portStatsPktsTx256to511Octets": "1.3.6.1.4.1.14179.1.4.1.1.5",
    "AIRESPACE-SWITCHING-MIB::portStatsPktsTx512to1023Octets": "1.3.6.1.4.1.14179.1.4.1.1.6",
    "AIRESPACE-SWITCHING-MIB::portStatsPktsTx1024to1518Octets": "1.3.6.1.4.1.14179.1.4.1.1.7",
    "AIRESPACE-SWITCHING-MIB::portStatsPktsRx1519to1530Octets": "1.3.6.1.4.1.14179.1.4.1.1.8",
    "AIRESPACE-SWITCHING-MIB::portStatsPktsTx1519to1530Octets": "1.3.6.1.4.1.14179.1.4.1.1.9",
    "AIRESPACE-SWITCHING-MIB::portStatsPktsTxOversizeOctets": "1.3.6.1.4.1.14179.1.4.1.1.30",
    "AIRESPACE-SWITCHING-MIB::switchingTraps": "1.3.6.1.4.1.14179.1.50",
    "AIRESPACE-SWITCHING-MIB::multipleUsersTrap": "1.3.6.1.4.1.14179.1.50.1",
    "AIRESPACE-SWITCHING-MIB::broadcastStormStartTrap": "1.3.6.1.4.1.14179.1.50.2",
    "AIRESPACE-SWITCHING-MIB::broadcastStormEndTrap": "1.3.6.1.4.1.14179.1.50.3",
    "AIRESPACE-SWITCHING-MIB::linkFailureTrap": "1.3.6.1.4.1.14179.1.50.4",
    "AIRESPACE-SWITCHING-MIB::vlanRequestFailureTrap": "1.3.6.1.4.1.14179.1.50.5",
    "AIRESPACE-SWITCHING-MIB::vlanDeleteLastTrap": "1.3.6.1.4.1.14179.1.50.6",
    "AIRESPACE-SWITCHING-MIB::vlanDefaultCfgFailureTrap": "1.3.6.1.4.1.14179.1.50.7",
    "AIRESPACE-SWITCHING-MIB::vlanRestoreFailureTrap": "1.3.6.1.4.1.14179.1.50.8",
    "AIRESPACE-SWITCHING-MIB::fanFailureTrap": "1.3.6.1.4.1.14179.1.50.9",
    "AIRESPACE-SWITCHING-MIB::stpInstanceNewRootTrap": "1.3.6.1.4.1.14179.1.50.10",
    "AIRESPACE-SWITCHING-MIB::stpInstanceTopologyChangeTrap": "1.3.6.1.4.1.14179.1.50.11",
    "AIRESPACE-SWITCHING-MIB::powerSupplyStatusChangeTrap": "1.3.6.1.4.1.14179.1.50.12",
    "AIRESPACE-SWITCHING-MIB::bsnSwitchingGroups": "1.3.6.1.4.1.14179.1.51",
    "AIRESPACE-SWITCHING-MIB::bsnSwitchingCompliances": "1.3.6.1.4.1.14179.1.52"
}
