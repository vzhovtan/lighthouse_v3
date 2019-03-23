from __future__ import unicode_literals, absolute_import, print_function
import bdblib
__copyright__ = "Copyright (c) 2017 Cisco Systems. All rights reserved."

#--------------------------------------------------------------------------
# LAST UPDATED: Nov. 10 2017 By Sergio
# ANYONE WORKING NOW: no one
#--------------------------------------------------------------------------


#--------------------------------------------------------------------------
#
# STANDALONE MODE:
# ===============
# Runs only on BDB, need to change the platform and technology as needed:
#
# https://scripts.cisco.com:443/ui/use/cs1_Lighthouse_backend?request=standalone&autorun=true&platform=ASR9K&technology=ACL
#
#
#
# GENERATE DROPDOWN:
# =================
# Generates JS code for the dropdown options:
#
# https://scripts.cisco.com/ui/use/cs1_Lighthouse_backend?request=generate&autorun=true
#
#--------------------------------------------------------------------------


def task(env, request, srNumber, problemDescription, platform, technology):
    result = bdblib.TaskResult()
    if(request == "guidance_by_Problem_Description"):
        result.append(analyzeProblemDescription(problemDescription), name="guidance")
    if(request == "guidance_by_technology"):
        result.append(analyzeTechnology(platform, technology), name="guidance")
    if(request == "standalone"):
        result.append(bdblib.HTML(analyzeTechnology(platform, technology)))
    if(request == "generate"):
        result.append(generateDropdown())
    return result

#--------------------------------------------------------------------------
# HTML TAGGING:
# ============
#
#  'http'      -- Hyperlink is detected. If the string/line is followed by '>' then the text that follows will be the hyper link text else the whoel hyperlink will be the text.
#  ']:' + '//' -- For comments on CLI commands. Add spaces after the command and the comments will be in gray color.
#  ']:'        -- Add line break after string/line.
#  ':' + '//'  -- For title with comments. Title will be in bold while the comments will be in gray
#  ':'         -- String/line in Bold and line break at the end.
#  '//'        -- For comments on CLI commands. Add spaces after the command and the comments will be in gray color.
#  '@'         -- email address. Creates mailto hyperlink for String/line.
#
#  default     -- Line break after String/line.
#--------------------------------------------------------------------------

def convertHTML(data):
    newData = ""
    for line in data.splitlines():
        if "http" in line:
            if ">" in line:
                text,link = line.rstrip().split(">",1)
                newData += "<li><a href='" + link.strip() + "'target='_blank'>" + text + "</a></li>"
            else:
                newData += "<li><a href='" + line + "'target='_blank'>" + line + "</a></li>"
        elif ("]:" in line) and ("//" in line):
            command,comment = line.rstrip().split("//",1)
            newData += command  + "&emsp;&emsp;&emsp;&emsp;<span style='color:grey;'>&nbsp;&nbsp;&nbsp;&nbsp;" + comment + "</span></br>"
        elif ("]:" in line):
            newData += line + "</br>"
        elif (("Useful Commands For Troubleshooting:" in line)| ("Support Links:" in line)) and ("//" in line):
            title,comment = line.rstrip().split("//",1)
            newData += "<u><h1><font size='3'></br>" + title + "</h1></font></u>" + "<i><span style='color:grey;'>&nbsp;&nbsp;&nbsp;&nbsp;" + comment + "</span></i></br></br>"
        elif ("Useful Commands For Troubleshooting:" in line)| ("Support Links:" in line):
            newData += "<u><h1><font size='3'></br>" + line + "</font> <h1></u></br>"
        elif (":" in line and "//" in line):
            title,comment = line.rstrip().split("//",1)
            newData += "<b>" + title + "</b>" + "&emsp;&emsp;&emsp;&emsp;<i><span style='color:grey;'>&nbsp;&nbsp;&nbsp;&nbsp;" + comment + "</span></i></br>"
        elif ":" in line:
            newData += "<b>" + str(line) + "</b></br>"
        elif "//" in line:
            command,comment = line.split("//",1)
            newData += command + "&emsp;&emsp;&emsp;&emsp;<span style='color:grey;'>&nbsp;&nbsp;&nbsp;&nbsp;" + comment + "</span></br>"
        elif "@" in line:
            newData += "<li><a href='mailto:" + line + "' target='_top'>Mailer : " + line + "</a></li>"
        else:
            newData +=  line + "</br>"
    return newData

def analyzeTechnology(platform, technology):
    result = "ERROR : Platform and technology not found."
    if (platform == "IOS-XR Platform Independent"):
        if technology in dict_PI:
            result = str(header(platform, technology)) + str(convertHTML(str(dict_PI[technology]))) + footer
        else:
            result = str(header(platform, technology)) + str(not_found) + footer
    if (platform == "ASR9K"):
        if technology in dict_ASR9K:
            result = str(header(platform, technology)) + str(convertHTML(str(dict_ASR9K[technology]))) + footer
        else:
            result = str(header(platform, technology)) + str(not_found) + footer
    if (platform == "CRS"):
        if technology in dict_CRS:
            result = str(header(platform, technology)) + str(convertHTML(str(dict_CRS[technology]))) + footer
        else:
            result = str(header(platform, technology)) + str(not_found) + footer
    if (platform == "GSR - 12K"):
        if technology in dict_GSR12000:
            result = str(header(platform, technology)) + str(convertHTML(str(dict_GSR12000[technology]))) + footer
        else:
            result = str(header(platform, technology)) + str(not_found) + footer
    if (platform == "NCS5000"):
        if technology in dict_NCS5000:
            result = str(header(platform, technology)) + str(convertHTML(str(dict_NCS5000[technology]))) + footer
        else:
            result = str(header(platform, technology)) + str(not_found) + footer
    if (platform == "NCS5500"):
        if technology in dict_NCS5500:
            result = str(header(platform, technology)) + str(convertHTML(str(dict_NCS5500[technology]))) + footer
        else:
            result = str(header(platform, technology)) + str(not_found) + footer
    if (platform == "NCS6K"):
        if technology in dict_NCS6000:
            result = str(header(platform, technology)) + str(convertHTML(str(dict_NCS6000[technology]))) + footer
        else:
            result = str(header(platform, technology)) + str(not_found) + footer
    if (platform == "eXR"):
        if technology in dict_eXR:
            result = str(header(platform, technology)) +str(convertHTML(str(dict_eXR[technology]))) + footer
        else:
            result = str(header(platform, technology)) + str(not_found) + footer
    if (platform == "7600"):
        if technology in dict_7600:
            result = str(header(platform, technology)) +str(convertHTML(str(dict_7600[technology]))) + footer
        else:
            result = str(header(platform, technology)) + str(not_found) + footer
    return result




def analyzeProblemDescription(problemDescription):
    # TBA LOGIC TO PARSE PD
    result = analyzeTechnology("ASR9K", "VSM")
    return result


def header(platform, technology):
    text = "<b><font size='4'><div id='LighthouseContentTitle' style='text-align:center'><h1>Lighthouse : " + str(platform) + " - " + str(technology) + "</h1></div></b></font><div id='LighthouseContentBody' style='background-repeat: no-repeat; background-position: right bottom; background-image: url(https://i.imgur.com/QpmaXol.jpg);'>"
    return text

footer = "</div><div id='LighthouseFeedback' align='right'><a href='mailto:lighthouse-csone@cisco.com?Subject=Lighthouse%20Feedback' target='_top'>Click here to provide feedback or suggest commands to be added.</a></div>"

def generateDropdown():
    code = ""
    code += "Copy and replace the options variable with the following code on the BJB script:\n"
    code += "https://scripts.cisco.com/ui/edit/cs1_Lighthouse\n\n"
    code += "var options = [\n"
    code += "          '<option value=\"\">-- select a technology --</option>'\n"
    code += "          , // IOS XR PI\n"
    x = 1
    for key in sorted(dict_PI.keys()):
        code += "          '<option value=" + key +">" + key +"</option>'"
        if x < len(dict_PI):
            x += 1
            code += "+\n"
        else:
            code += "\n"
    code += "          , // ASR9K\n"
    x = 1
    for key in sorted(dict_ASR9K.keys()):
        code += "          '<option value=" + key +">" + key +"</option>'"
        if x < len(dict_ASR9K):
            x += 1
            code += "+\n"
        else:
            code += "\n"
    code += "          , // CRS\n"
    x = 1
    for key in sorted(dict_CRS.keys()):
        code += "          '<option value=" + key +">" + key +"</option>'"
        if x < len(dict_CRS):
            x += 1
            code += "+\n"
        else:
            code += "\n"
    code += "          , // GSR - 12000\n"
    x = 1
    for key in sorted(dict_GSR12000.keys()):
        code += "          '<option value=" + key +">" + key +"</option>'"
        if x < len(dict_GSR12000):
            x += 1
            code += "+\n"
        else:
            code += "\n"
    code += "          , // NCS 5000\n"
    x = 1
    for key in sorted(dict_NCS5000.keys()):
        code += "          '<option value=" + key +">" + key +"</option>'"
        if x < len(dict_NCS5000):
            x += 1
            code += "+\n"
        else:
            code += "\n"
    code += "          , // NCS 5500\n"
    x = 1
    for key in sorted(dict_NCS5500.keys()):
        code += "          '<option value=" + key +">" + key +"</option>'"
        if x < len(dict_NCS5500):
            x += 1
            code += "+\n"
        else:
            code += "\n"
    code += "          , // NCS 6K\n"
    x = 1
    for key in sorted(dict_NCS6000.keys()):
        code += "          '<option value=" + key +">" + key +"</option>'"
        if x < len(dict_NCS6000):
            x += 1
            code += "+\n"
        else:
            code += "\n"
    code += "          , // eXR\n"
    x = 1
    for key in sorted(dict_eXR.keys()):
        code += "          '<option value=" + key +">" + key +"</option>'"
        if x < len(dict_eXR):
            x += 1
            code += "+\n"
        else:
            code += "\n"
    code += "          , // 7600\n"
    for key in sorted(dict_7600.keys()):
        code += "          '<option value=" + key +">" + key +"</option>'"
        if x < len(dict_7600):
            x += 1
            code += "+\n"
        else:
            code += "\n"
    code += "      ];"
    return code





dict_PI = {
                   'AIB Adjacencies' : """
                              Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
                              show cef adjacency loc []
                              show adjacency summary
                              show adjacency internal location []
                              show adjacency detail location []
                              show adjacency detail hardware location []
                              show adjacency remote internal location []
                              show adjacency remote detail location []
                              show adjacency quarantine-list location []  //(View deleted Tx adj on node)
                              show adjacency quarantine-list remote location []   //(View deleted Rx adj on node)
                              show adjacency quarantine-list client-info location [] //(View deleted Tx adj and client(s) holding locks to it )
                              show adjacency quarantine-list remote client-info location [ node-id ]  //(View deleted Rx adj and client(s) holding locks to it )
                              show adjacency consumer detail location []
                              show adjacency producer detail location []
                              show adjacency [ interface type ] [ interface number ] remote internal detail location []
                              show imds interface brief
                              show imds interface [inteface type] [interface numner] | include ifhandle

                              AIB Traces:
                              show adjacency trace [] location [] //("all" trace doesn't include imdr and slow traces)
                              show adjacency hardware trace location  []
                              show adjacency trace slow location []
                              show platform aib trace all location []

                              AIB debugs:
                              debug aib events location []
                              debug aib update location []
                              debug aib table location []
                              debug aib errors location []
                              debug aib imdr location []

                             Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
                             Techzone - IOS XR AIB Generic AIB debugging guide > https://techzone.cisco.com/t5/IOS-XR-PI-Forwarding-Infra-Eng/IOS-XR-AIB-Generic-AIB-debugging-guide/ta-p/1048029
                             Wiki - AIB > http://wiki-eng.cisco.com/engwiki/AIB
                             Wiki - IOS XR AIB > http://wiki-eng.cisco.com/engwiki/IOS_2dXR_2dAIB
                             Wiki - AIB triage diagnostics > https://wiki.cisco.com/display/IOXFORWARD/AIB%20triage%20diagnostics
                             iox-aib@cisco.com
                             """,

                         'APS' : """
                             Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
                             show clock   // Multiple Router - APS, correlated logs based on time stamps
                             show ntp status
                             show process sonet_aps_agent location []  //(executed on both Working and Protect routers.)
                             show process sonet_aps_manager
                             show process block location []  // (working and Protect if different)
                             show interface serial * accounting location [node-id] //(issue command on the APS Disabled slot/line)
                             show controller sonet [sonet line] sonetmib farendline-history interval all
                             show controller sonet [sonet line] sonetmib line-history interval all
                             show controller sonet [sonet line] sonetmib path-history interval all
                             show aps agents    // (shows remote peer , local agent , groups)
                             show run controller sonet [ line number ] // (for Work/Protect )
                             show run int pos [ line numeber ] // ( for Work/Protect )
                             show aps group [ group number ]
                             show controller sonet [ line number ] // ( for Work/Protect )
                             show int pos [ line numer ] // (for Work/Protect )

                             show tech-support [ aps, gps, pos ]
                             admin show tech-support shelf-management
                             show tech-support spa location [] // (for Working / Protect if different )
                             show tech-support aps terminal

                             APS Traces / Debugs: //( Issue for all slots where links , groups exsist for Work / Protect )

                             show aps partner trace reverse location []
                             show aps agent trace reverse location []
                             show aps manager trace reverse
                             show sonet-local trace reverse location []
                             show sonet-local trace error location []
                             show sonet-local trace info location []
                             show sonet-local trace init reverse location []
                             show cema trace reverse location []
                             show t3 trace reverse loc []
                             show t1 trace location []
                             show transport trace location []

                             debug sonet aps error location []
                             debug sonet aps event location []
                             debug sonet aps pgp location []
                             debug sonet aps wp-comm location []

                             Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
                             XRGeeks - CRS APS Troubleshooting > http://xrgeeks.cisco.com/?q=content/crs-aps-troubleshooting
                             Techzone - Understanding and Troubleshooting POS SONET DWDM MR APS Chalk > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Understanding-and-Troubleshooting-POS-SONET-DWDM-MR-APS-Chalk/ta-p/108208
                             Ask ASR9K - Troubleshooting APS > http://asr9k.cisco.com/ask/index.php?action=artikel&cat=12&id=486&artlang=en
                             q-sonet@cisco.com
                             q-sonet-dev@cisco.com
                             """,
                         'ARP' : """
                            Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
                            show arp
                            show arp traffic location []
                            show arp resolution history location []
                            show arp api-stats  //(all the system API's usinf ARP and states)
                            show arp status location []
                            show arp idb all location []   //(internal data base configurations related to ARP)
                            show adjacency detail hardware location []
                            show tech-support arp

                            Traces/Debugs:
                            show arp trace location []
                            show adjacency trace all location []
                            show adjacency trace all errors location []
                            show cef trace location []

                            debug arp events
                            debug arp errors
                            debug all

                            Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
                            Wiki - ARP Troubleshooting > http://enwiki.cisco.com/ARP/Troubleshooting
                            Techzone - Debugging ARP Protocol Issues on ASR9K > https://techzone.cisco.com/t5/ASR-9000/Debugging-ARP-Protocol-Issues-on-ASR9K/ta-p/944150
                            xr-arp-support@cisco.com
                             """,
                          'BFD' : """
                                Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
                                show bfd
                                show bfd client
                                show bfd client history
                                show bfd [ipv4 | ipv6] session
                                show bfd session detail
                                show bfd session detail interface [ type ] [ number ]
                                show bfd all session detail location []
                                show bfd all session status detail location []
                                show bfd all session status history location []
                                show bfd counters
                                show bfd counters packet interface [ type ] [ number ]
                                show bfd counters all packet interface [ type ] [ number ]
                                show bfd counters all packet invalid location []
                                show bfd statistics private location []
                                show bfd counters packet private detail location []
                                show lpts pifib hardware static-police location []

                                BFD over Bundles:
                                show bfd counters ipv4 packet interface [ type ] [ number ] //on all bundle members, Check if both sides sending BFD packets.
                                show bfd bundles echo detail location []
                                show bfd bundles detail location []
                                show bfd all session detail //The session type field should say RTR_BUNDLE

                                Debugs/show-tech/traces:
                                show tech-support routing bfd
                                show tech bundles  //for BFD over bundles
                                show bfd trace fsm location []
                                show bfd trace location []
                                debug bfd [ process | error | lib | client-api ]
                                debug bfd trace bfd_ip_echo_xmt location []

                                Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
                                Cisco Support Forums - BFD Support Doc> https://supportforums.cisco.com/document/144626/bfd-support-cisco-asr9000
                                IETF - RFC5880 > http://tools.ietf.org/html/rfc5880
                                cisco doc central - BFD white paper > http://wwwin-eng.cisco.com/Eng/OIBU/X/Test_Plans_Rpts/IOS-XR-c12k-BFD-White-Paper.doc
                                Cisco Support - ASR 9000 Series Routing Configuration guide > http://www.cisco.com/en/US/docs/routers/asr9000/software/asr9k_r4.2/interfaces/configuration/guide/hc42bifw.html
                                Techzone - BFD over TE troubleshooting > https://techzone.cisco.com/t5/ASR-9000/ASR9K-BFDoTE-Troubleshooting/ta-p/972533
                                Wiki - BFD troubleshooting > https://wiki.cisco.com/display/GSRTR/C12000+BFD
                                Wiki - BFD over Bundles troubleshooting steps > https://wiki.cisco.com/display/GSRTR/C12000+BFD+Over+Bundles
                                Doc central - bfd support for multihop, mpls-lsps, pws and virtual/tunnel/bundle interface > http://wwwin-eng.cisco.com/Eng/OIBU/IOS_XR_PI/Presentations/BFD-Design.ppt
                                Techzone - BFD session over bundle VLAN (BVLAN) > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/BFD-session-over-bundle-VLAN-BVLAN-with-Alcatel/ta-p/63754
                                iox-bfd-dev@cisco.com
                                q-bfd-coders@cisco.com
                                q-bfd@cisco.com
                             """,
                             'Crash' : """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show log
								show logging location []
                                show pfm location all
								show version
								admin show install active summary
								admin show install commit summary
								show placement
								show process [ process name ] location []
								show process log location []
								show reboot last syslog location []
								show reboot last crashinfo location []
								show reboot history location []
								show processes aborts location all
								show context
								show media 		 	//  to find attach media
                                dir /recurse [media]: location all  | inc [month day time ]    // search for files on the media created at the card crash time details

                                Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
                                Techzone - Troubleshooting IOS XR Process Crashes And Tracebacks  > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Troubleshooting-IOS-XR-Process-Crashes-And-Tracebacks/ta-p/77098
                                Cisco Eng - Troubleshooting IOS XR Process crashes > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/q-tac/Troubleshooting/Crashes/xr_crashes.html
                                Wiki - Essential crash info. > http://enwiki.cisco.com/IoxServiceInfra/DevTest/EssentialCrashInformation
                                Cisco Eng - Troubleshooting crashes > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/q-tac/Troubleshooting/Crashes/iox_crash.pdf
                                BDB scripts - xr_stack_decoder link > https://scripts.cisco.com/ui/use/xr_stack_decoder
                                Techzone - Decoding IOS-XR traceback on SMU/Service Pack/Feature Pack enabled router > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Decoding-IOS-XR-traceback-on-SMU-Service-Pack-Feature-Pack/ta-p/836054
                                Cisco Eng - Decode Kernel Dump > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/q-tac/Troubleshooting/Crashes/kernel_dump.txt
                                Cisco Eng - Interpretting Crash info. > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/q-tac/Troubleshooting/Crashes/kernel_crashinfo_interpreter.txt
                              """,
                            'BGP' : """
                            	Useful Commands For Troubleshooting:  //( Some commands syntax could vary according to platform or version)
								show bgp      // ( shows bgp table, use filters for specific details )
								show run router bgp
								show bgp [afi,safi] A.B.C.D [/pfxlen]     // ( for all commands afi ipv4/ipv6/all, safi unicast/multicast/all )
								show bgp [afi,safi] A.B.C.D[/pfxlen] longer-prefixes     //  ( all the routes which are more specific than the prefix specified )
								show bgp [[afi] [safi]] neighbors [ ip-addr/len ] routes      // all the routes received from this neighbor
								show bgp [[afi] [safi]] unknown-attributes                           // any attributes for route not understood by the local system
								show bgp [[afi] [safi]] dampened-paths   // routes suppressed due to dampening, not routes withdrawn by advertising neighbor
								show bgp [[afi] [safi]] flap-stat                                            // flap statistics of routes, maintained only if dampening is enabled
								show install which component bgp                                        // can be other BGP process types when installed
								show bgp all all summary
								show bgp all all nsr
								show bgp all all proces  perf detail
								show bgp all all nsr stand
								show bgp all all proces perf detail stand
								show bgp trace wrapping
								show tcp dump-file all location [ RP ACTV/STBY ]
								show bgp trace | beg  [ month day hr ]                            // (use begin to limit date and time of the issue troubleshooting )
								show tech-support routing bgp
								show tech-support tcp nsr

								BGP Routes:
								show bgp x.x.x.x/y bestpath-compare
								show bgp vrf [ vrf name]  [ ipaddr/len ]
								show bgp nexthops
								show rib firsthop [ ipaddr/len ]              // (look if we have both RPs as clients)
								show bgp nexthop [ ipaddr/len ]               // (for the affected nexthop)
								show bgp nexthops perf-stats
								show bgp ipv4 labeled-unicast neighbors [ ipaddr/len ] advertised-routes
								show bgp ipv4 labeled-unicast neighbors [ ipaddr/len ] routes
								show svd role                    // can impact what routes are downloaded to nodes

								Neighbors:
								show bgp neighbors        // (peering sessions, afi/safi , prefixes, performance, configuration, inheritance)
								show bgp [[afi] [safi]] neighbors [ ipaddr/len ]
								show bgp [[afi] [safi]] neighbors                                      // all neighbors
								show bgp [[afi] [safi]] neighbors [ ipaddr/len ] performance-stat     // messages tx / rx from neighbor, time spent processing those messages
								show bgp [[afi] [safi]] neighbors [ ipaddr/len ] configuration          // configs, settings inherited from af-groups, neighbor/session groups
								show bgp [[afi] [safi]] neighbors [ ipaddr/len ] inheritance             // session-group the neighbor inherits configuration settings
								show bgp [[afi] [safi]] summary                                          // all the neighbors for AFI/SAFI configured
								show bgp all all summary
								show bgp neighbor [ ipaddr/len ] configuration

								BGP Debugs: // (some debugs can consume CPU, reference to documentation and get customer approval before running debugs)
								dumpcore running [jid for bgp process] location []             //  active/standby RP's  , recommended to get before escalation
								debug bgp all                                                  //  All BGP debugs
								debug bgp ?                                     // BMP Family , Communication library, Dampening if enabled, events, keepalive,
																				// Label, nexthop, policy-execution, postit, rpki, sync, table, update
								debug bgp i?                                    // BGP import processing, Choose a particular BGP instance AS, input/output
								debug bgp rib                                   //  BGP interaction with IP RIB

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Techzone - IOS XR Troubleshooting steps > https://techzone.cisco.com/t5/ASR-9000/IOS-XR-BGP-Troubleshooting-steps/ta-p/805366
								Techzone - Troubleshooting IOS XR BGP Common Problems > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Troubleshooting-IOS-XR-BGP-Common-Problems/ta-p/260738#anc6
								Techzone - BGP Troubleshooting Engineering Wiki > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/BGP-Troubleshooting-Engineering-Wiki/ta-p/892599#anc0
								Wiki - BGP Troubleshooting Information > http://wiki-eng.cisco.com/engwiki/BGP_20Troubleshooting_20Information
								Cisco Support - Troubleshooting High CPU Caused by the BGP Scanner or BGP Router Process > http://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/107615-highcpu-bgp.html
								Jive - BGP Flags > https://cisco.jiveon.com/docs/DOC-66192
								IETF - RFC4271 - A Border Gateway Protocol 4 (BGP-4) > https://tools.ietf.org/html/rfc4271
								Cisco Tool - BGP Message Decoder > http://wwwin-routing.cisco.com/cgi-bin/bgp_decode/bgp_decode.pl
								cs-xr-bgp@cisco.com q-bgp-dev@cisco.com
                                """,
                            'VPLS' : """
                                Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show bgp neighbor
								show l2vpn discovery bridge-domain
								show l2vpn bridge-domain detail
								show l2vpn bridge-domain autodiscovery bgp detail
								show bgp l2vpn vpls
								show l2vpn atom-db       // (Peer ID, Source, VC ID,  Encap,  SIG,  FEC, AD)
								show  l2vpn forwarding bridge-domain [bridge-domain-name] mac-address location [loc]                    // (To display the summary information for the MAC address)
								show l2vpn discovery xconnect
								show l2vpn xconnect mp2mp detail
								show bgp l2vpn vpws

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
                                Techzone - BGP-based VPLS Autodiscovery on XR > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Configuring-and-Troubleshooting-BGP-based-VPLS-Autodiscovery-on/ta-p/358125
                                ASR9K L2VPN and Ethernet Services Configuration Guide > https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/asr9k_r4-1/lxvpn/configuration/guide/lesc41/lesc41p2mps.html#wp1317421

								cs-xr-bgp@cisco.com
                                """,
                           'BGP RPL' : """
                           Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show run rpl
								show rpl maximum             // (Current total,limit,Max Limit of Lines , policies configured, )
								show process policy_repository
								show sysdb registrations verification job [ policy_repository ] shared-plane         // (registration logs showing Time, jid, nid, tid, handle, reg_path)
								show rpl route-policy [ policy ] uses all            // (shows other policy sets directly or indirectly applied to this policy)
								show rpl route-policy [ policy ] reference           // (list all the policies that reference the named policy)
								show rpl route-policy [ policy ] attach           // (display all policies used at an attach point for named policy )
								show rpl route-policy [policy] detail
								show pcl protocol bgp speaker-0 export [ attach point instance ] policy profile
								show rpl trace clientlib file /tmp/ltrace/policy_clientlib/bgp-speaker-0 original location []
								show tech-support routing rpl [ attachpoint instance ] policy profile

								Debugs:
								debug bgp policy-execution internal route-policy [name]
								debug bgp policy-execution run vrf [name]
								debug pcl profile detail

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - RPL > https://wiki.cisco.com/display/SPRSG/RPL
								Wiki - RPL page > http://wiki-eng.cisco.com/engwiki/RplPage
								q-rpl-coders@cisco.com
                                """,
                           'BGP Memory Utilization' : """
                           		Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
                                // BGP will bring down peering once the threshold reaches major level, BGP process would exit once critical threshold is reached.
								show log |inc MEMORY_       // alarms generated when physical memory usage reaches thresholds, 75% (minor alarm), 85% (major), 95% (critical)
								show memory summary location all      //  (check available physical memory )
								show proc bgp                         // (get job id, make sure process is running)
								show processes memory
								show bgp vrf all summary
								show bgp all all summary
								show route summary
								show route ipv6 summary
								show route vrf all ipv6 summary
								show proc bgp
								show mem [ Job ID from show proc bgp ]
								show mem heap dllname  [Job ID ]  // (collected these 2 commands - 5 times at 30 min intervals)
								show dll jobid [ Job ID ]
								show bgp all all process perf detail location []  // (if table size remains same comparing the difference between the snapshots)
								show watchdog memory-state location []
								show watchdog threshold memory defaults location []
								show watchdog threshold memory configured location []
								show process memory
								show memory summary

								show watchdog trace
								show bgp process det
								show bgp scale

								show bgp all all process detail    // (to get amount of prefixes and paths stored on the system )
								show bgp vrf all  process detail   // (to get amount of prefixes and paths stored on the system)

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Techzone - Troubleshooting IOS XR BGP Common Problems > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Troubleshooting-IOS-XR-BGP-Common-Problems/ta-p/260738#anc6
								cs-xr-bgp@cisco.com
                                """,
                           'BGP AD Auto Discovery' : """
                                Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show  bgp neighbor
								show  l2vpn discovery bridge-domain
								show  l2vpn bridge-domain detail
								show  l2vpn bridge-domain autodiscovery bgp detail
								show  bgp l2vpn vpls
								show  l2vpn atom-db       //   ( Peer ID, Source, VC ID,  Encap,  SIG,  FEC, AD )
								show  l2vpn forwarding bridge-domain [bridge-domain-name] mac-address location [loc]                    // (To display the summary information for the MAC address)
								show  l2vpn discovery xconnect
								show  l2vpn xconnect mp2mp detail
								show  bgp l2vpn vpws

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Techzone - Troubleshooting IOS XR BGP Common Problems > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Configuring-and-Troubleshooting-BGP-based-VPLS-Autodiscovery-on/ta-p/358125
								cs-xr-bgp@cisco.com
                                """,
                           'CFM OAM' : """
                           		Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show ethernet cfm summary
								show ethernet cfm local meps
								show ethernet cfm local maintenance-points
								show ethernet cfm peer meps detail
								show ethernet cfm configuration-errors
								show ethernet cfm interfaces statistics
								show ethernet cfm interfaces status
								show ethernet cfm ccm-learning-database
								show ethernet cfm traceroute-cache status complete
								show ethernet cfm traceroute-cache status incomplete
								show tech-support ethernet protocols platform cfm
								show tech-support ethernet protocols oam

								show ethernet cfm trace process all
								debug ethernet cfm packets interface [ type ] [ number ] received full

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - Ethernet OAM/CFM Quick Reference > http://enwiki.cisco.com/EthernetOam/Cfm
								Cisco Support - Configuring Ethernet OAM and CFM > http://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst4500/15-1/XE_330SG/configuration/guide/config/E_OAM.pdf
								ASR 9K Series Aggregation Services Router Interface and Hardware Component Configuration guide > http://cisco.com/en/US/docs/routers/asr9000/software/asr9k_r3.9/interfaces/configuration/guide/hc39eoam.html
								Cisco Support - Cisco IOS Carrier Ethernet Command Reference > https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/cether/command/ce-cr-book/ce-s1.html
								iox-cfm-dev@cisco.com
                                """,
                           'CfgMgr configuration' : """
                           		Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
                                //!! DO NOT use cfs check or clear config inconsistency, CLI may clear issues
								show log | inc consistency         //(look for conf error, inconsistency)
								show health cfgmgr
								show configuration [ options ]     //(Some of the options will need more sub options to get relevant outputs)
								show config failed startup         //(displays configa that failed when start/boot up. See if the commands failed due to sematic/syntax/apply error)
								show config failed                 //(failed during the last commit operation)
								admin show config failed startup
								admin show config failed
								show configuration persistent      //(difference between the running configuration and persistent configuration)
								show configuration persistent diff    //(check if there is a difference between the running configuration and the persistent configuration)
								show shelfmgr status location []
								show process blocked location []     //(commit is taking time or timing out, check if cfhmgr-rp is blocked on sysdb/rdsfs_svr etc)
								show redundancy                      //(Standy RP may not be ready as the cfg may not be applied on Stby-RP)
								show configuration history           //(history of all configuration events)

								Trace / Show Tech:
                                show cfgmgr trace
								show sysdb trace client-errors location []               //(run on RP or LC)
								show hw-module trace all level detailed reverse location []
								show cfgmgr trace wr rev location [] file [media]:[filename]
								show tech sysdb location [] file [media]:[filename]
								show tech cfgmgr location [] file [media]:[filename]
								show tech shelfmgr

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - IOXCfgMgr/InitialTriage > http://wiki-eng.cisco.com/engwiki/IOXCfgMgr_2fInitialTriage
								Wiki - IOXCfgMgr/Guidelines/ConfigLoss > http://wiki-eng.cisco.com/engwiki/IOXCfgMgr_2fGuidelines_2fConfigLoss
								Wiki - EngWiki User Preferences IOXCfgMgr/Guidelines/FAQ > http://wiki-eng.cisco.com/engwiki/IOXCfgMgr/Guidelines/FAQ
								Wiki - IOXCfgMgr > http://wiki-eng.cisco.com/engwiki/IOXCfgMgr#RaisingIssues
								iox-pi-infra-triage@cisco.com
								q-cfgmgr-dev@cisco.com
								interest-q-cfgmgr@cisco.com
                                """,
                           'Environment' : """
                                Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								admin show environment [ all | current | fan | power | temperatures | trace | voltages ] [ location ]
								show logging events buffer bistate-alarms-set
								admin show logging onboard temperature location []
								admin show environment trace

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Cisco Support - System Monitoring Command Reference for Cisco ASR 9000 Series Routers > https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/system_monitoring/command/reference/b-sysmon-cr-asr9k/b-sysmon-cr-asr9k_chapter_01.html#wp3676047718
                                """,
                           'High CPU' : """
                           		Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								terminal exec prompt timestamp                //( Ensures time stamps are printed the show output )
								top dumbtty                                   //( This command keeps running , allow to collect a few sample - the ext cntrl-c )
								show process cpu location [] | exc 0% 0% 0%     //( issue command multiple times )
								dumpcore running [ jid ] location []            // !! Be careful !! If output is too big, sometimes this can cause RP failover

                                Process issue:
								show process block location []                  //( issue multiple times )
								show process [ process_name ] location []
								follow process [ pid ] location []

                                Multiple Processes Causing High CPU: //!! IPC involves gsp or sysdb. By monitoring these processes to find out which process is causing high cpu
								show processes cpu | exclude 0% 0% 0%            //( issue multiple times )
								show gsp stats client                            //( Get multiple snapshot and compare the results )
								show sysdb connections shared-plane              //( Displays the client connection information for sysdb and shared-plane data )
								show sysdb trace edm shared-plane tailf          //( tailf option displays new traces as they are added, cntrl-c to stop )

                                BGP High CPU:
								show bgp all all process performance detail     //( verify BGP scale, # prefixes, paths and path-elements, estimate of bgp table scale )
								show bgp [ afi ] [ safi ] summary | inc main    //( rate of churn, collect 10 times at 30 sec interval. normal churn,
																				//  ~ 100 version/min normal, If ] 1000/min, can cause CPU spike )
								show bgp all all sum | inc "table|family"       //( shows abnormal churn in the network same as above )
								show bgp vpnv4 unicast vers  [current version ] [ max of the version number ]   //( To find out vpnv4 uni networks versions changing rapidly. Check those networks )

                                //!!If not related to churn, flapping interface etc then continue below:

								top d                                                           //( for a period of 5 min , then cntl-c to stop,k will show top consumers of CPU )
								show process [bgp_jid] location [node-id]                            //( jid found from show process, look for import, update, label, rib-update threads )
								show process threadname [bgp_jid] location [node-id]                //( RP where active BGP process is running, low timers )
								follow job [bgp_jid] stackonly iteration 20 delay 1            //( creates 20 trace back output with triggering process in threads )
								bgp vrf all summary | inc "VRF:|RD|main"                       //( BGP table version is smaller than any prefix version in that table )
								show show bgp trace | inc wrapped                                //( version wrap beyond 32-bit version can cause BGP high CPU )

                                Memory Issue: // !! some commands do not have location option, may need to run in shell for those cases
								show process memory location []
								show process memory [ jid ] location []  //( issue multiple times to see if its size is growing, jid found in show process command )
								show memory heap dllname [ jid ]   //( issue multiple times )
								show process file [ jid ] detail

								Memory Compare Tool:
								show memory compare start     //( Wait some time to allow changes to occur )
								show memory compare end
								show memory compare report

                                Traces and Debugs: //!! Commands will be according to the process causing the high CPU
								show cef [ ipv4|ipv6|mpls ] trace   //( Collect if cpu is high due to fib_mgr )
								show tech gsp   //( Collect if cpu is high due to gsp process )

                                Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - PI High CPU Utilization or CPU Hog > https://wiki.cisco.com/display/GSRTR/PI+High+CPU+Utilization+or+CPU+Hog
                                Wiki - Troubleshooting High CPU Utilization > http://wwwin-iox.cisco.com/wiki/doku.php/lighthouse:infra:debug:case1
								Case - High CPU troubleshooting > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/q-tac/Troubleshooting/CPU/CPU-Trobleshoot.txt
								Techzone - Troubleshooting High CPU Utilization in IOS XR > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Troubleshooting-High-CPU-Utilization-in-IOS-XR/ta-p/85638
								Cisco Support - Troubleshooting High CPU Caused by the BGP Scanner or BGP Router Process > http://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/107615-highcpu-bgp.html
								Wiki - BGP is using high CPU > http://wiki-eng.cisco.com/engwiki/BGP_20Troubleshooting_20Information#head-268b1f231dc468d2021e04dea96e5c431aa9c218
                                """,
                           'IGMP Snooping' : """
                           		Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show igmp snooping summary
								show igmp snooping summary statistics
								show igmp snooping port detail
								show igmp snooping port [ type ] [ numner ] detail
								show igmp snooping port group                        //( Show groups within ports )
								show igmp snooping profile
								show igmp snooping profile references
								show igmp snooping group                             //( Displays IGMP group membership information )
								show igmp snooping group summary
								show igmp snooping group address [ ipaddr/len ]
								show igmp snooping bridge-domain [bridge-domain-name] [detail[statistics[[include-zeroes]   //( Displays IGMP snooping config. info / traffic statistics for bridge domain )

								show l2vpn forwarding mroute ipv4 location []      //( Displays multicast routes in the forwarding tables for certain location ]
								show l2vpn forwarding mroute ipv4 group [a.b.c.d] location []
								show l2vpn forwarding bridge-domain mroute ipv4 hardware ingress location []
								show L2vpn forwarding bridge-domain mroute ipv4 hardware egress detail location []
								show mgid client mapping   //( To display all the clients joined to the multicast group in a specific multicast group identification(MGID) )
								show uidb data location [] [ type ] [ number ] ingress

								show igmp snooping trace all
								debug igmp snooping all
								show tech igmp snooping          //( add keyword terminal to display the output on terminal )

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Techzone - IGMP snooping debug output explanation > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/IGMP-snooping-debug-output-explanation/ta-p/177184
								Wiki - IGMP RFCs > https://wiki.cisco.com/display/SPRSG/IGMP+RFCs
								Wiki - IGMP Snooping Tutorials > https://wiki.cisco.com/display/SPRSG/IGMP+Snooping+Tutorials
								Wiki - IGMPSN TOI > https://wiki.cisco.com/display/SPRSG/IGMPSN+TOI
								iox-igmp-snoop-dev@cisco.com
                                """,
                              'IPC' : """
                                Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show aipcproxy statistics pcid list     //( statistics data for proxys connections and memory usage for source pcid in local aipc_proxy )
								show aipcproxy statistics pcid [0 - 4096] connection     // statistics data for proxys connections and memory usage for specific pcid
								show ipc p2p trace p2p-ipc process [ proc_name ] instanceid [] option all
								show ipc p2p trace p2p-ipc process [ proc_name ] instanceid [] option init
								show ipc p2p trace p2p-ipc process [ proc_name ] instanceid [] option conn
								show ipc p2p trace p2p-ipc process [ proc_name ] instanceid [] option ctrl
								show ipc p2p trace p2p-ipc process [ proc_name ] instanceid [] option msg

								show shmalloc trace jid [job id ] all
								show tech-support p2p-ipc process [ proc_name ] instance-id []
								show tech aipcproxy

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - P2P Async IPC Project > http://wiki-eng.cisco.com/engwiki/P2P_20Async_20IPC_20Project?action=show#head-77f1807fac556e21f88ecf66ed7b4e80a903f69f
                                """,
                             'IPv6' : """
                             	Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show ipv6 interface
								show ipv6 interface [ type ] [ number ]
								show ipv6 bundle nodes
								show ipv6 bundle interfaces location []
								show ipv6 neighbors summary
								show ipv6 neighbors location []
								show ipv6 traffic
								show ipv6 lisp statistics
								show ipv6 trace [ ea, io, ma, nd, netio ]

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Techzone - Overview and Troubleshooting IPv6 Neighbor Discovery in XR > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Overview-and-Troubleshooting-IPv6-Neighbor-Discovery-in-XR/ta-p/425807
								Exteral - 6PE / 6vPE  TOI > http://frankenberry/gbc/elearn/content/iosxr/6PE6vPE_TAC_TOI.pptx
								cs-ipv6@cisco.com
								q-ipv6-dev@cisco.com
                                """,
                             'ISIS' : """
                                Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show isis
								show isis neighbors
								show isis topology
								show isis statistics
								show isis statistics bundle-ether [ number ]
								show isis adjacency-log
								show isis interface bundle-ether [number]
								show clns statistics

								show isis trace all
								show tech-support routing isis terminal
								debug isis adjacencies [interface FOO]

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - ISIS troubleshooting > https://wiki.cisco.com/display/ASOPSSUP/ISIS%20troubleshooting
								Wiki - ISIS troubleshooting2 > http://wiki-eng.cisco.com/engwiki/IS-IS/TroubleShooting
								Wiki - isis issues > http://wwwin-iox.cisco.com/wiki/doku.php/lighthouse:is-is:debug
								Wiki - ISIS > https://wiki.cisco.com/display/SPRSG/IS-IS
								ISIS FAQ > http://wwwin-deployment.cisco.com/training/isis/dw-isis-faq.html
								cs-iox@cisco.com cs-clns@cisco.com cs-iprouting@cisco.com
                                """,
                           'LPTS' : """
                           		Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show lpts pifib hardware entry location []
								show lpts pifib brief location []
								show lpts pifib hardware entry statistics location []
								show lpts pifib hardware police location []
								show placement program all | in lpts                 //( Program Active and Standby state, JID, Active location)
								show lpts binding brief                              //( Individual client requests. Displays what the applications are asking for. Verify the bindings )
								show lpts clients                                    //( Client id,  location, flags,  open flags )
								show lpts flows brief
								show lpts ifib slices all
								show lpts ifib entry brief
								show lpts ifib statistics location []             //( Valid only for RP )
								show lpts ifib                                    //( Displays the authoritative database and the counters for secondary look-ups )
								show lpts pifib entry brief location []           //( Pre-ifib in LC/RP (netio) (SW), Type, VRF-ID, L4, Interface, Deliver Local-Address Port, Remote-Address Port )
								show lpts pifib entry location []                 //( Pre-ifib in LC/RP (netio) (SW) , other related statistics and counters, drops , SYNC )
								show lpts pifib hardware entry brief location []              //( TCAM in LC only (HW), pre-IFIB hardware table )
								show lpts pifib hardware entry statistics location []         //( TCAM in LC only (HW), drop counters )
								show lpts pifib hardware usage location []                    //( TCAM in LC only (HW) )
								show lpts pifib hardware police location []                   //( TCAM in LC only (HW) )
								show controllers pse statistics loc []                      //( Non LPTS traffic and counters on Packet Switching Engine LC )

								Debugs/Traces:
								show lpts trace global                            //(  proc start, slice assigment, dependecies )
								show lpts trace ff                                //( LPTS Flow Forwarder (Pre-IFIB manager) )
								show lpts trace fgid                              //( LPTS FGID-DB library )
								show lpts trace fm                                //( LPTS Flow Manager )
								show lpts library
								show lpts pa                                      //( LPTS Port Arbitrator trace )
								show lpts platform
								show tech-support lpts
								debug lpts packet slow-path location []
								deb lpts packet slow-path location []            //!! Lots of outputs, be careful !!
								debug netio drivers location []

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - LPTS-Local Packet Transport Service > https://wiki.cisco.com/display/SPRSG/LPTS-Local%20Packet%20Transport%20Service
								Wiki - IFIB troubleshooting commands > http://wiki-eng.cisco.com/engwiki/IFIB
								Wiki - Troubleshooting LPTS > https://techzone.cisco.com/cisco/attachments/cisco/xr_other@tkb/154/1/LPTS_Tshooting.pdf
								Cisco Support - LPTS commands > https://www.cisco.com/c/en/us/td/docs/routers/crs/software/crs_r4-1/addr_serv/command/reference/b_ipaddr_cr41crs/b_ipaddr_cr41crs_chapter_0111.html#wp3562882238
                                """,
                           'Memory Leak' : """
                           		Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version) //!! Some commands may not have a location option, run in shell if needed
								show memory summary location all              //( Per node , application, image, reserved, IOmem, flash, total shared window memory )
								show memory summary detail location all       //( More details on shared window allocations and other memory usages per node )
								show watchdog memory-state location []                 //( Show physical, free, memory and its state per location )
								show watchdog threshold memory defaults location all   //( Shows setting for memory threshold alerts, some the system can take action on )
								show process memory location []      //( Shows top users of application memory, sorted highest user to lowest, only the first lines are important )
								show process memory [ jid ] location []       //( Issue multiple times,  see if its size is growing, JID is from show process name )
								show mem [ jid ]                              //( Displays the available physical memory / memory usage information of processes )
								show memory heap dllname [ jid ]              //( Issue multiple times, groups memory blocks by allocator PC,  sorts based on total memory size )
								show dll jobid [ jid ]               //( Displays dynamically loadable library (DLL) information for the specified job identifier (jid) of block.)
								show process file [ jid ] detail     //( Displays information about active processes for open files and open communication channels )
								show shmwin summary

								Memory usage analyzer:
								show memory compare start    //( Allow some time, as memory can change base on other events )
								show memory compare end
								show memory compare report

								show watchdog trace
								dumpcore running [ jid ] location []

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - IOXMemoryLeaks > http://wiki-eng.cisco.com/engwiki/IOXMemoryLeaks
								Wiki - EngWiki  MemUsage > http://wiki-eng.cisco.com/engwiki/MemUsage
								Cisco Support - Troubleshooting Memory Leaks > http://wwwin-people.cisco.com/chanvija/memleak.htm
								Cisco Support - Memory-related Triage Help > http://wwwin-people.cisco.com/kkataria/material/memory.html
								Techzone - Troubleshooting Memory Leaks in IOS XR > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Troubleshooting-Memory-Leaks-in-IOS-XR/ta-p/85658
								Cisco docs - Process and Memory Management Commands on Cisco IOS XR Software > https://www.cisco.com/c/en/us/td/docs/routers/xr12000/software/xr12k_r3-9/system_management/command/reference/yr39xr12k_chapter11.html#wp910777591
                                """,
                           'MLDP' : """
                           		Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version) //( Multicast Label Distribution Protocol )
                                show pim vrf mc context private detail
								show mpls mldp database brief
								show mpls mldp database [ LSM ID ]
								show mrib vrf mc route [ group ] private detail
								show mrib encap-id [ encap Identifier value ]  //( From show mrib vrf mc route [ group ] )
								show mpls forwarding lsm-id [ LSMID value ] detail private

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Techzone - Configure mVPN Profiles within Cisco IOS-XR > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Configure-mVPN-Profiles-Within-Cisco-IOS-XR/ta-p/600292
								Techzone - mVPN IOS-XR Specifics >https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/mVPN-IOS-XR-Specifics/ta-p/757451
								Techzone -  mLDP Fundamentals  > https://techzone.cisco.com/t5/MPLS/mLDP-Fundamentals/ta-p/726863
								Techzone - Configure mVPN Profiles within Cisco IOS-XR > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Configure-mVPN-Profiles-Within-Cisco-IOS-XR/ta-p/600292
                                """,
                           'MPLS' : """
                           		Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								Forwarding information:
								show mpls forwarding labels [ start_label ] [ end_label ] detail location []
								show mpls forwarding hardware [ egress | ingress ] label range [ start_label ] [ end_label ] location []
								show mpls forwarding hardware [ egress | ingress ] label [ number ] location []
								show mpls forwarding hardware [ egress | ingress ] label all location []
								show mpls forwarding label [label] hardware [ingress|egress] location []
								show mpls forwarding label [label] private hardware [ingress|egress] location []

								LDP:
								show mpls ldp bindings [ ipadrr/len ]
								show mpls ldp bindings [ ipadrr/len ] detail
								show mpls ldp neighbor brief
								show mpls ldp neighbor [ type ] [ number ]
								show mpls ldp  discovery [ type ] [ number ]

								show route [ ipv4 | ipv6 ]
								show route [ ipv4 | ipv6 ] detail

								CEF / MPLS :
								show cef [ ipv4 | ipv6 ] [ ipaddr/len ] detail location []
								show cef [ ipv4 | ipv6 ] [ ipaddr/len ] hardware [ ingress | egress ] detail location []
								show cef [ ipv4 | ipv6 ] detail
								show cef adjacency [ type ] [ number ] hardware [ingress | egress]  loc []
								show cef mpls [ ipv4 | ipv6 ] [ ipaddr/len ] detail location []
								show cef mpls [ ipv4 | ipv6 ] [ ipaddr/len ] hardware [ ingress | egress ] detail location []
								show cef mpls [ ipv4 | ipv6 ] detail
								show cef mpls adjacency [ type ] [ number ] hardware [ingress | egress]  loc []  //( To show the MPLS tunnel adjacency )

								show tech-support mpls ldp location [] terminal     //( Active RP )

								Traces:
								show mpls ldp  trace [ binding, error, config, discovery, forwarding, gr, igp-sync, interface, nsr, peer, process,route, targeted, wrapping ] | [location]]
								show cef trace [ errors, events, table ]
								show cef platform trace mpls all wrapping location all
								show cef platform trace te all wrapping location all
								show cef mpls trace wrapping location all
								show cef mpls trace
								show cef mpls trace [ table, error, events ]
								show rib ipv4 trace
								show rib ipv4 trace wrapping
								show attribute trace
								show im trace

								Show Techs:
								show tech-support cef
								show tech-support cef mpls detail location []        //( Active RP )
								show tech-support cef ipv4 detail
								show tech-support pfi all

								LDP Debugs
								debug  mpls ldp discovery hello send interface [ type ] [ number ]
								debug  mpls ldp discovery hello receive interface [ type ] [ number ]

                                Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - IOS-XR MPLS LDP > http://wiki-eng.cisco.com/engwiki/IOS_2dXR_20MPLS_20LDP
								Wiki - MPLS Forwarding information > http://wiki-eng.cisco.com/engwiki/MPLS_20Forwarding_20information
								Wiki - IOS-XR MPLS OAM Troubleshooting > http://wiki-eng.cisco.com/engwiki/IOS_2dXR_20MPLS_20OAM_20Troubleshooting
								Doc Central - MPLS Forwarding Troubleshooting guide > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/q-tac/Troubleshooting/MPLS/Forwarding/MPLS_Forwarding_Troubleshooting_Guide.doc.html
								Techzone - Tracing a path from one CE to another through a MPLS Network (IOS XR) > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Tracing-a-path-from-one-CE-to-another-through-a-MPLS-Network-IOS/ta-p/385031/message-revision/385031:1
								Techzone - Tracing LDP to MPLS TE labels on a P router > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Tracing-LDP-to-MPLS-TE-labels-on-a-P-router/ta-p/129306
								Techzone - Troubleshooting Duplicate addresses being advertized by multiple MPLS LDP peers > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Troubleshooting-Duplicate-addresses-being-advertized-by-multiple/ta-p/390841
								Wiki - FIB triage diagnostics > https://wiki.cisco.com/display/IOXFORWARD/FIB+triage+diagnostics

								mpls-ldp-xr-support@cisco.com
								q-mpls-lsd@cisco.com
                                """,
                           'MPLS TE Traffic Engineering' : """
                           		Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show mpls traffic-eng tunnels name [ tunnel name ]   //( Status, Parameters, History, Path Info for tunnel )
								show mpls traffic-eng tunnels p2mp
								show mpls traffic-eng link-management admission-control   //( Tunnels admitted locally and parameters )
								show rsvp session
								show mrib route
								show mrib ipv6 route
								show mpls forwarding
								show mpls forwarding p2mp
								show mpls forwarding p2mp detail
								show mpls forwarding detail
								show mpls forwarding tunnels      //( Tunnel(s) at head end , label, interface, next hop, bytes )
								show mpls forwarding labels
								show mpls forwarding labels [ label ] hardware egress detail location []    //( Use local label )
								show mpls traffic-eng tunnels tabular
								show mpls traffic-eng topology path tunnel  [ tunnel id ]

								Fast ReRoute
								show mpls traffic-eng fast-reroute database
								show mpls traffic-eng fast-reroute database location []
								show mpls traffic-eng fast-reroute log
								show mpls forwarding detail    //( Should see backup tunnel )
								show rsvp fast-reroute
								show mpls traffic-eng tunnel role mid detail
								show mpls traffic-eng tunnel property fast-reroute
								show mpls traffic-eng tunnel protection
								show mpls traffic-eng tunnel backup
								show mpls traffic-eng forwarding
								show mpls traffic-eng server protected-interface

								TE FastReRoute: //( Logs to collect )
								show mpls forwarding tunnels

								BFD:
								show mpls traffic-eng link-management bfd-neighbors

								Backup Tunnels:
								show mpls traffic-eng forwarding
								show mpls traffic-eng tunnels tabular
								show mpls traffic-eng auto-tunnel backup
								show mpls traffic-eng tunnels backup
								show mpls traffic-eng tunnels backup protected-interface name [ type ] [ number ]

								Mapping Labels:
								show mpls forwarding tunnels                      //( Shows  label for tunnel )
								show mpls forwarding                              //( Shows local label )
								show cef [ ipaddr/len ] hw ingress location []    //( Ingress LC should point to TE with TE label )
								show mpls forwarding hw egress label [ label value ] location []  //( Looks for egress label programming )
								show mpls traffic-eng forwarding

								show tech-support mpls traffic-eng terminal
								show tech-support mpls rsvp terminal

								Trace: //Collect below set of commands on ingress node where traffic is redirected onto tunnels and the tunnel is head and Tail end )
								show mpls traffic-eng trace
								show cef platform trace te err location []
								show cef platform trace te all location []
								show cef platform trace common err location []
								show cef platform trace all all location []
								show cef platform trace mpls all wrapping location all
								show cef platform trace te all wrapping location all
								show cef trace location []
								show cef trace err location []
								show mpls traffic-eng trace [ errors, buffer, client, default, events, interface ]
								show rsvp trace wrapping location all

								Debugs:
								debug mpls traffic-eng [ events, tunnels state, tunnels events, tunnels signal ]
								debug rsvp signaling
								debug rsvp dump-messages bundle brief sub-message
								debug rsvp dump-messages all brief

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Topic Search - How does LSP MTU work > http://topic.cisco.com/news/cisco/ce/cs-rrr/msg06031.html
								Wiki - TE Troubleshooting - FRR > https://wiki.cisco.com/display/XRTE/TE+Troubleshooting+-+FRR
								Wiki - RSVP-TE Basics > https://wiki.cisco.com/display/XRTE/RSVP-TE+Basics
								Techzone - TE and RSVP support: general requirements > https://techzone.cisco.com/t5/IOS-XR-PI-MPLS-TE-RSVP-Eng/TE-and-RSVP-support-general-requirements/ta-p/1056160
								Wiki - TE Troubleshooting - Tunnel Down > https://wiki.cisco.com/display/XRTE/TE%20Troubleshooting%20-%20Tunnel%20Down
								Wiki - TE Troubleshooting - Flooding and Topology Issues > https://wiki.cisco.com/display/XRTE/TE%20Troubleshooting%20-%20Flooding%20and%20Topology%20Issues
								Cisco - MPLS TE commands > https://www.cisco.com/c/en/us/td/docs/routers/crs/software/crs_r4-1/mpls/command/reference/b_mpls_cr41crs/b_mpls_cr41crs_chapter_011.html#wp7040847600
								mpls-te-xr-support@cisco.com
                                """,
                           'Multicast' : """
                           		Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
                                IGMP:
								show igmp groups [ type ] [ number ]               //( Group Membership , Address, Interface, Uptime, Expires, Last Reporter )
								show igmp groups [ type ] [ number ] all-joins      //( S,G info and state )
								show igmp traffic                                 //( Counters and errors for IGMP related traffic )
								show mhost groups [ type ] [ number ]    //( Groups joined on interface mhost, manages group memberships for processes )

                                PIM:
								show pim interface [ type ] [ number ]    //( Ip Address, Interface, PIM states, Nbr count, hello interval, DR Priority, DR info )
								show pim interface [ type ] [ number ] | inc on   //( On this system PIM should be "on" status )
								show pim neighbor                         //( Neighbor Address, Interface, Uptime, Expires, DR,  primary, Flags )
								show pim group-map                        //( Check mcast group mapping between PIM mode and its RP info )
								show pim rpf                              //( Check RPF interface to RP or Source address and interface )
								show pim topology [ Source/Group ip addr ] detail    //( PIM-SM topology has [*,G] entry and [S,G] entry,
                                                                                  // [S,G] SPT could have different RPF than [*,G], PIM-SSM topo has [S,G] )

                                clear pim topology [ Source/Group ip addr ]       //( Resets all Group entries in PIM topology pim, rpf RP or Source address )

                                Interface enabled with Multicast in SW and HW:
								show mfib interface [ type ] [ number ] detail location []
								show mfib hardware interface detail [ type ] [ number ] location []        //( Interface Handle, Ghandle, Enbld ( should be true) )
								show uidb data location [] | in MULTICAST         //( Ipv4 and ipv6 Multicast, ACL, Boundry, 1 = enabled, 0 = disabled )

								Multicast  Consistency between SW and HW forwarding entry:
								show mrib route [ S,G ] detail        //( Version/FGID #'s , ingress/outgoing interface (A=accept, F=forwarding), Uptime )
								show mfib route [ S,G ] detail        //( Check version/FGID consistency between mrib/mfib/HW mfib, Counters, Flags, Uptime )
								show mfib route [ S,G] ] detail location []    //( On ingress lincard, check FGID, Flags, Route ver, Counters, Uptime )
								show mfib hardware route olist detail [ S,G ] location []  //( On ingress lincard )
								show mfib hardware route olist shadow [ S,G ] location []  //( On ingress LC, shadow memory ingress LC HW mfib )
								show mfib hardware route olist hex-dump [ S,G ] location []  //( on ingress LC, compare LC memory shadow mfib and real LC HW Hex mfib )
								show mrib fgid info [ fgid number ]   //( FGID, Context ( S,G mapped to this fgid), reference #, # = LC members) )
								admin show controllers fabric fgid information id [ fgid # ] //( Verify the FGID programming in fabric, olist interface in egress LC's, FGID
																							 associated fabricq Ids )
								admin show controllers fabric fgid information id [ fgid # ] diagnostics    //( Verify FGID hardware Hex programmed info )
								show mfib route [ S,G ] detail location []  //( Egress LC, outgoing interface should have EG flag on egress LC, flags )
								show mfib hardware route olist detail [ S,G ] location []  //( Egress LC, ONull false = olist no Null egress interface )
								show mfib hardware route olist shadow [ S,G ] location []  //( Egress LC shadow memory )
								show mfib hardware route olist hex-dump [ S,G ] location [] //Egress LC, compare shadow with real HW hex same as ingress )

								clear mfib database location []  //( Clear mfib database to force re-sync from mrib, impact transient traffic drop)

								Multicast packets statistic: // ( Check traffic forwarding bps/pps, if forwarding statistic is moving, drop counter should not increase )
								show interface [ type ] [ number ] | in multicast     //( Ingress interface L2 packets statistic )
								show interface [ type ] [ number ] | in drop
								show interfaces [ type ] [ number ] accounting        //( Check ingress / egress interface L3 accounting )
								show mfib route rate [ S,G ]                         //( Source,Group traffic forwarding bps, pps )
								show mfib counter location []   //( Mfib counter statistics for packets dropped, failure counters ( not incrementing))
								show mfib route statistics detail [ S,G ] location []   //( Ingress/egress LC forwarding statistic, SW Failure, HW Drop and Rates )
								show mfib hardware route statistics detail [ S,G ] location []  //( LC HW forwarding statistic, drops, rates )
								clear  [pim], [mfib], [interface]  //( to clear any statistical counters, or establishow a baseline to compare )

								Trace commands:
								show pim trace
								show mrib trace error                           //( Mrib; mcast routing database info )
								show mrib trace
								show mrib platform trace [ error, event, info ]
								show mfib trace error loc []                   //( Mfib; mcast forwarding database info )
								show mfib trace loc []
								show mfib hardware trace [ error, warning, route ] loc []
								show mfib hardware trace all loc []
								show mlib trace [ warning, error, idb, interface, netio, route ] loc []   //( Mlib; route and interface management )

								show tech-support multicast

								follow process [ name ]
								dumpcore running [ jid or process name ]
								show install which component [ name ]         //( Shows where, state running or not running on )

								Mulitcast over Bundle:
								bundle-hashow bundle-[ type ] [ number ]   //( Check which bundle member interface is [S,G] selected to forwarding traffic )
								show mrib route [ S,G ]     //( Which LC (S,G) traffic is forwarded on Outgoing Interface List , OIL )

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Cisco Case - Multicast commands outputs > http://wwwin-people.cisco.com/rtamaela/TAC/XR%20Multicast/Multicast%20command_output.txt
								Techzone - mVPN Rosen Draft Cheat Sheet > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/mVPN-Rosen-Draft-Cheat-Sheet/ta-p/99352
								Wiki - Multicast Troubleshooting Commands Cheat Sheet > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/q-tac/Troubleshooting/Multicast/multicast_cheat_sheet.html
                                Techzone - Configure mVPN Profiles within Cisco IOS-XR  > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Configure-mVPN-Profiles-Within-Cisco-IOS-XR/ta-p/600292
								Wiki - Troubleshooting MVPN > http://wwwin-iox.cisco.com/wiki/doku.php/lighthouse:multicast:mvpn
                                Wiki - Troubleshooting Multicast > http://wwwin-iox.cisco.com/wiki/doku.php/lighthouse:multicast
                                Techzone - mVPN Master Page > https://techzone.cisco.com/t5/MPLS/mVPN-Master-Page/ta-p/630356
								q-multicast-dev@cisco.com
								crs-multicast-support@cisco.com
								x-multicast-triage@cisco.com
								iox-igmp-snoop-dev@cisco.com
								""",
                           'MSDP' : """
                           		Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show msdp summary        //(  Displays peer status, address, autonomous system, state, Up/downtime, SA sent or received )
								show msdp globals        //(  AS , Caching, originator (RP), default peer (When RPF fails), Active RP, counters, buffers )
								show msdp peer           //( Stats on peer - filters, status, counters )
								show msdp rpf
								show msdp sa-cache
								show msdp statistics peer
								show msdp vrf [ vrf name ] statistics peer
								show msdp vrf [ vrf name ] rpf [ host name or IP ]
								show msdp vrf [ vrf name ] ipv4 summary
								show msdp vrf [ vrf name ] ipv4 statisics
								show msdp vrf [ vrf name ] ipv4 rpf [ host name or IP ]
								show msdp vrf [ vrf name ] summary
								show msdp process
								show route multicast
								show bgp ipv4 multicast
								show route ipv4 multicast
								show msdp rpf [ prifix RPF address or hostname ]
								show bgp ipv4 multicast nexthops [ prefix of next hop ]   //( MSDP peers must be known in Border Gateway Protocol (BGP) )

								show msdp trace | in [ perfix of interest ]

								debug msdp peer  [peer address ]
								debug msdp io  [ peer address ]

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Techzone - MSDP Peer RPF Rules > https://techzone.cisco.com/t5/Routing-Protocols/MSDP-Peer-RPF-Rules/ta-p/747889
								Cisco Support - IP Multicast: PIM Configuration Guide > http://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipmulti_pim/configuration/12-4/imc-pim-12-4-book/imc_msdp_im_pim_sm.html
								Support Forums - Introduction to IOS XR Multicast > https://supportforums.cisco.com/document/100301/introduction-ios-xr-multicast
								Techzone - Multicast Routing - MSDP and PIM walk through > https://techzone.cisco.com/t5/Multicast/Multicast-Routing-MSDP-and-PIM-walk-through/ta-p/811663
                                Wiki - Troubleshooting Multicast > http://wwwin-iox.cisco.com/wiki/doku.php/lighthouse:multicast
								Cisco Support - Using MSDP to Interconnect Multiple PIM-SM Domains  > http://www.cisco.com/en/US/docs/ios-xml/ios/ipmulti_pim/configuration/12-4/imc_msdp_im_pim_sm.html#GUID-2ACB5E5E-F70B-4795-8513-DB8208B76B88
								Wiki - Multicast Troubleshooting Commands Cheat sheet > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/q-tac/Troubleshooting/Multicast/multicast_cheat_sheet.html
								q-multicast-dev@cisco.com
								crs-multicast-support@cisco.com
                                """,
                           'NetIO debug' : """
                           		Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show netio chains [ type ] [ number ] location []
								show netio trace all  location []
								show netio chains fiNT location []    //( Shows chains, protocol type/number, packet/bytes dropped per protocol )

								Debugs: // ( Debug nodes into the data chains in NetIO. When packets pass through these nodes, they are counted and logged )
								netio-debug add 77 ifname FINT0/RSP0/CPU0 [ protocol chain name] decap before lpts log location []
								netio-debug log-drop 77 offset 0 length 1024 dump location []             //( action for the instance # where the chain was defined )
								netio-debug remove all location []
								show netio-debug trace location []

								Packets for Ping Testing Recieve :
								netio-debug add 7 [ type ] [ number ] base decap before ether log location []
								netio-debug add 7 [ type ] [ number ] ipv4 decap before ipv4 log location []
								netio-debug log-drop 7 offset 0 length 64 detail dump location []
								netio-debug filter 7 1 ingress-interface [ type ] [ number ] location []
								netio-debug filter 7 1 offset 32 length 4 value 02020800 location []
								show netio-debug trace location []

								Packets for Ping Testing Transmit - Sent from Forwarding Interface FINT:
								sh netio idb all brief location []
								sh netio idb FINT location []
								netio-debug add 7 ifname FINT0/0/CPU0 ipv4 encap before ipv4 log location []
								netio-debug log-drop 7 offset 0 length 64 detail dump location []
								netio-debug remove all location []

								CDP:
								netio-debug add 7 [ type ] [ number ] ether_sock encap before ether_sock log location []
								netio-debug log-drop 7 offset 0 length 64 detail dump location []

								ISIS: // ( Packets handled by RSP )
								debug netio drivers location [RP] pakdumplevel 3 direction from-all interface [ type ] [ number ]    //( From sub-intf / main intf )

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - Netio Debug Nodes > http://enwiki.cisco.com/InterfaceManager/TroubleShooting/Data/Netio/DebugNodes
								Wiki - Troubleshooting Data Plane > http://enwiki.cisco.com/InterfaceManager/TroubleShooting/Data
								iox-netio@cisco.com
                                """,
                       'NSR Non-Stop Routing' : """
                       								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show nsr ncd client all location []                  //( NSR Consumer Demuxer for all clients )
								show nsr ncd queue [ low|all ] location []           //( NSR Consumer Demuxer consumer QAD queues LOW priority queue counter / errors )
								show cerrno library trace reverse
								show cerrno server trace reverse
								show cerrno server location [] all
								show lpts ifib slice stat
								show netio clients
								show packet summary

								Multicast:
								show pim nsf
								show mfib ipv4 nsf                                                     //( State normal )
								show mfib ipv4 nsf location []

								OSPF:
								show ospf                                  //(  NSR (Non-stop routing) is Enabled )
								show ospf statistics nsr                   //( multiple counter and statistics Issue more than once )
								show ospf standby interface brief
								show ospf standby neighbor
								show nsr ncd queue brief                  //( NSR low/high Queue, Total packets, accepted packets )
								show nsr ncd client brief                 //( Pid, Protocol, Instance,  Total Packets/Acks, Accepted Packets/Acks )
								show nsr ncd client all                   //( Client Protocol, counters , Issue more than once )

								TCP:
								show tcp statistics summary
								show tcp statistics
								show tcp counter state [ state name ]                   //( Issue ? after state to see all of the options for state )
								show tcp detail pcb all location []
								show tcp brief                                          //( Check Recv-Q, Send-Q, State )
								show tcp brief | inc prefix                             //( PCB hex value )
								show tcp packet-trace                                   //( PCB found in the previous command )
								show tcp detail pcb [ same PCB ]
								show tcp dump-file all loc []                           //( Process is running active RP/RSP )
								show tcp detail pcb
								show tcp trace nsr error reverse location []
								show tcp nsr brief
								show tcp nsr client brief
								show tcp nsr statistics summary location []
								show tcp nsr statistics client all
								show tcp nsr statistics pcb [ pcb # ]

								MPLS:
								show mpls ldp nsr summary
								show mpls ldp nsr stat

								L2VPN:
								show l2vpn nsr private [ standby ]
								show l2vpn session-db private [ standby ]
								show l2vpn events [ standby ]
								show l2vpn bridge private [ standby ]
								show l2vpn xconnect private [ standby ]
								show process bgp detail location all
								show redundancy trace verbose location all
								show processes tcp detail location []
								show processes bgp detail location []

								show tcp trace nsr error verbose location all
								show tcp trace nsr event verbose location all
								show bgp trace location []
								show tcp trace location []
								show tech tcp nsr
								show tcp dump-file list all location [ standby_node ]

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - IOXNRS/NRSTroubleshootingGuide > http://wiki-eng.cisco.com/engwiki/IOXNRS_2fNRSTroubleshootingGuide
                                """,
                           'NTP' : """
                           		Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show log | inc ntp
								show ntp drift                                               //( Key , dift measured time )
								show ntp associations                                  //( Ip address, ref clock ip, st, when, poll, reach, delay, offset, disp values )
								show ntp associations detail
								show ntp associations location all
								show ntp associations detail location [ [ slot ] | all ]
								show ntp status                                             //( General stats , intervals, delay )
								show ntp status location [ [ slot ] | all ]
								show ntp history
								show ntp history location [ [ slot ] | all ]
								show calendar                                                     //( System calendar )

								show ntp trace
								show ntp trace loc []

								debug ntp core
								debug ntp internal
								debug ntp packets

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								output description
								Cisco Support - Network Time Protocol (NTP) Issues Troubleshooting and Debugging Guide > http://www.cisco.com/en/US/tech/tk648/tk362/technologies_tech_note09186a0080c163a0.shtml
								Cisco Support - Verifying NTP Status with the show ntp associations Command > http://www.cisco.com/en/US/products/sw/iosswrel/ps1818/products_tech_note09186a008015bb3a.shtml
								q-ntp@cisco.com
								cs-ntp@cisco.com
                                """,
                           'OSPF' : """
                           		Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show run router ospf                               //( Router id, other configurations and setting )
								show ospf [ process id ]
								show ospf [ process id ] interface brie
								show ospf [ process id ] neighbor
								show ipv4 interface brief  | inc [ interface-name ]
								show ospf [ process id ] interface [ type ] [ number ]
								show ospf [ process id ] statistics interface [ type ] [ number ]
								show ospf [ process id ] statistics [ prot , nsr, spf ]       //( Packet counters for protocol. nsr, spf issue multiple times )
								show ospf [ process id ] database database-summary            //( Database summary for  each area, process, summary for count, delete, max age
								show ospf retransmission-list
								show ospf request-list                                        //( Router is trying to request a particular database update, age )
								show ospf database router
								show ospf message-queue
								show ospf statistics raw-io
								show ospf statistics prot
								show ospf summary
								show packet-memory summary

								ITAL://(Interface and Table Attribute Library, single point of contact for getting interface and VRF/table attributes for applications )
								show ital dbase if-dbase all process ospf-risc location []
								show ital dbase if-dbase [ type ] [ number ] process ospf-ldg location []
								show ital trace reverse

								show ospf trace all                    //( a lot of out put use more specific request if known after " trace " ( rib, bgp etc ) and last X lines )
								show ospf [ process  id ] trace idb 100    //( 100 would give last 100 lines  ( 1-32768 ) )
								show ospf [ process  id ] trace ital 100
								show raw trace reverse verbose

								show tech-support routing ospf file [ media:file name ]
								show tech-support routing ospfv3 detail file [ media:file name ]
								show tech-support pfi
								show tech-support lpts
								show tech-support cef

								OSPF VRF: //( CE-PE )
								show ipv4 vrf [ name ] interface [ type ] [ number ]
								show ospf vrf [ name ] [ area id ]
								show ospf vrf [ name ] [ area id ] vrf [ vrf name ] interface [ type ] [ number ]

								Debug: //( Increase ospf trace size buffer under ospf configuration submode for trace being ran to allow enough storage)
								debug ospf 1 trace detail spf external
								debug ospf 1 trace detail topology

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - OspfTroubleshootMain > http://wiki-eng.cisco.com/engwiki/OspfTroubleshootMain
								Techzone - OSPF Quick Reference > https://techzone.cisco.com/t5/Routing-Protocols/OSPF-Quick-Reference/ta-p/92510
								Cisco support - OSPF Design Guide > http://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/7039-1.html
                                """,
                           'OSPFv3' : """
                           		Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								sh run router ospfv3                                             //( Ospf instance, and various configurations )
								sh processes ospfv3
								sh ospfv3 [ ospf instance ] statistics interface [ type ] [ number ]          //( Counters , issue more than once looking for errors )
								sh ospfv3 [ ospf instance ] statistics prot
								sh ospfv3 [ ospf instance ] request-list [ type ] [ number ]                  //( Show the request list )
								sh ospf [ ospf instance ] database router  [ router-id ] internal
								sh ospf [ ospf instance ] vrf [ vrf name ] database router [ router-id  internal
								sh tech-support routing ospfv3 detail terminal
								sh ospfv3 neighbor [ type ] [ interface number ]

								sh ospfv3 [ ospf instance ] trace idb
								sh ospfv3 trace all

								Debug: // ( Increasing trace buffer size to allow for enough space when using debugs )
								debug ospfv3 [ ospf instance name ] [ ospf area acl, adj, bfd, chkpt etc ]

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Support Forums - Troubleshooting OSPFv3 Neighbor Adjacencies > https://supportforums.cisco.com/document/98581/troubleshooting-ospfv3-neighbor-adjacencies
								Cisco Support - OSPFv3 Commands on Cisco IOS XR Software > http://www.cisco.com/c/en/us/td/docs/ios_xr_sw/iosxr_r3-7/routing/command/reference/rr37osp3.html
								Cisco Support - Implementing OSPF on Cisco ASR 9000 Series Routers > http://www.cisco.com/en/US/docs/routers/asr9000/software/routing/configuration/guide/rcasr9kospf.html
								Docs - NSF--OSPF (RFC 3623 OSPF Graceful Restart) > http://www.cisco.com/c/en/us/td/docs/ios/12_0s/feature/guide/gr_ospf.html
								Cisco Support - Implementing OSPF on Cisco ASR 9000 Series Routers > http://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/routing/configuration/guide/rcasr9kospf.html#wp1247162
                                """,
                           'PFI Packet Forwarding Infrastructure' : """
                           		Useful Commands For Troubleshooting:   //( Some commands syntax could vary according to platform or version)
								show  im status                        //( Error, Informational conditions, issue may be gone if recovered, checks states)
								show  im resource-descriptions brief location all
								show  im history operations location []
								show  im database interface bundle-[ type ] [ bundle id ]
								show  im dampening                                          //( Interface, Protocol )
								show  im database brief location all                        //( Handle, Name, State, MTU, Views )
								show  im database verbose all
								show  im history system                                     //( Time, Node, Event, First seen, Count )
								show  im history operations brief location []
								show  im internals all location all
								show  im registrations all location all
								show  im registrations summary location all
								show  im resource-descriptions brief location all
								show  im statistics client location all
								show  im statistics server location all

								show  tech-support pfi

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - Interface Infrastructure Architecture > http://enwiki.cisco.com/InterfaceManager/Architecture
								Wiki - PFI Troubleshooting >http://enwiki.cisco.com/InterfaceManager/Troubleshooting
                                """,
                           'PPP' : """
                               	Useful Commands For Troubleshooting:    //( Some commands syntax could vary according to platform or version)
								show  proc blocked location []
								show  ppp statistics summary location []
								show  ppp summary location []

								PPP interface:
								show  ppp interfaces
								show  ppp interface [ type ] [ number ]
								show  ppp ea interface [ type ] [ number ]
								show  ppp statistics interface [ type ] [ number ]
								show  interface [ type ] [ number ]
								show  im chains [ type ] [ number ]
								show  netio chains [ type ] [ number ]
								show  adjacency location []

								show  tech-support ppp

								Traces:
								show  ppp trace location []
								show  im trace all location all
								show  chdlc trace all location []                //( Changing encapsulation )

								Debugs:
								debug ppp negotiation                             //( Negotiating, related to packet I/O )
								debug ppp packet
								debug condition interface [ type ] [ number ]     //( Use help filter outputs )

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Techzone - Multilink PPP for IOS-XR  > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Multilink-PPP-for-IOS-XR/ta-p/113246
                                """,
                        'PTP IEEE1588' : """
                        		Useful Commands For Troubleshooting:  //( Some commands syntax could vary according to platform or version)
								show  ptp interfaces brief
								show  ptp interfaces [ type ] [ number ]
								show  ptp interfaces summary
								show  ptp packet-counters bundle-[ type ] [ number ]
								show  ptp advertised-clock
								show  ptp local-clock
								show  ptp foreign-masters best
								show  ptp ma database
								show  ptp platform servo
								show  frequency synchronization selection
								show  frequency synchronization interfaces brief

								show  ptp trace packet location []
								show  tech-support ptp

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - IOS-XR PI PTP - Troubleshooting > http://enwiki.cisco.com/PTP/Troubleshooting
								Wiki - IOS-XR PI Frequency Synchronization - Troubleshooting > http://enwiki.cisco.com/FrequencySynchronization/TroubleShooting
								xr-freq-time-support@cisco.com
								xr-freq-time-dev@cisco.com
                                """,
                           'RIB' : """
                           		Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show route            //(  displays the RIB database )
								show route summary
								show rib table        //( VRF/Table, SAFI, Table ID, PrfxLmt, PrfxCnt, TblVersion, flags Yes/No for deleted, prefix/table limit )
								show rib protocols
								show rib hist        //( JID, Client (CID), Location process running ( example mpls_ldp), routing info, update, paths, timestamp )
								show rib clients
								show rib clients redistribution
								show rib clients redistribution hist
								show rib clients protocols
								show rib statistics [ rib client protocol example - ospf ]
								show connected ipv4 topology
								show connected interfaces
								show bcdl queues

								show lpts bindings client-id tcp
								show lpts trace [ ff , fm , global, pa , platform ] wrapping location all
								show ipv6 trace [ io, ma, nd, netio ] location all
								show bcdl trace file [ media/filename ]
								show rib trace [ media/filename ]
								show rib trace bcdl  [ media/filename ]
								show static ipv4 trace [ media/filename ]
								show static ipv6 trace [ media/filename ]

								RIB Client Commands: //( RIB ] FIB, add the missing or problem route prefix to commands )
								show arp
								show cef  [ prefix ]  //( Add missing or problem route )
								show cef ipv4 [ prefix ] detail
								show cef ipv4 [ prefix ] detail loc []
								show cef ipv4 [ prefix ] hardware [ ingress | egress ] detail location []
								show cef ipv4 unresolved
								show cef ipv4 unresolved location []
								show cef ipv4 unresolved location []
								show cef misc location []                        //( repeat 2 times 30 secs apart )
								show cef resource detail location []
								show cef trace
								show cef platfrom trace all all location []
								show cef trace location []

								show mpls forwarding prefix [ prefix ]
								show mpls ldp bindings [ prefix ]
								show mpls lsd forward detail
								show rcc ipv4 unicast [ prefix ] vrf default
								show mpls forwarding location []
								show cef mpls trace location []

								show ospf neighbor
								show ospf database
								show ospf database self-originate
								show ospf database router [ OSPF ID of the Adjacent neighbor ]
								show ospf retransmission-list
								show ospf request-list
								show ipv4 int [ flapped intf type ] [ Interface number ]

								show bgp trace rib

								show tech cef
								show tech arp
								show tech mpls ldp location [ active RP ]
								show tech mpls ldp location []
								show tech-support routing ospf terminal

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - IOX FIB Convergence (IFC) > http://wiki-eng.cisco.com/engwiki/IOX_20FIB_20Convergence_20_28IFC_29
								Wiki - FIB triage diagnostics > https://wiki.cisco.com/display/IOXFORWARD/FIB%20triage%20diagnostics
								Doc Central - RIB Troubleshooting presentation > http://wwwin-eng.cisco.com/Eng/OIBU/IOS_XR_PI/Presentations/RIB-troubleshooting.pptx
								Techzone - Which prefixes are flapping in the RIB (and maybe causing an high cpu) > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Which-prefixes-are-flapping-RIB-and-maybe-causing-an-high-cpu/ta-p/85928
                                q-rib-dev@cisco.com
                                """,
                           'RPL' : """
                           		Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show  rpl  prefix-set [ prefix set name ] references             //( Display the attach points, show ows all policies that use this object )
								show  rpl  prefix-set pfx_[ prefix set name ] attachpoints       //( Display the attach points, show ows all policies with vrf name )
								show  rpl  route-policy [ Route Policy name ] attachpoints
								show  rpl  route-policy [ Route Policy name ]                    //( show ow rpl route-policy, route-policy attached, vrf and ip address )
								show  rpl [inactive|active] route-policy
								show  rpl as-path-set states
								show  rpl community-set
								show  rpl ospf-area-set
								show  rpl maximum                                                //( show ow limits and current usage )
								show  rpl                                                        //( show ow configured rpl )
								show  run route-policy

								show  rpl trace client-registration
								show  rpl trace clientlib
								show  rpl trace dynamic-registration

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Jive - IOX BGP RPL ( Route Policy Language ) > https://cisco.jiveon.com/docs/DOC-1807580
								Support Forums - ASR9000/XR: Understanding and using RPL  (Route Policy Language) > https://supportforums.cisco.com/document/88676/asr9000xr-understanding-and-using-rpl-route-policy-language
                                """,
							'Convergence, Performance and Responsiveness': """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								BGP Convergence:
								show bgp convergence                                                      //( verify routing table with a particular AFI/SAFI has converged)
								show bgp [[afi][safi]] convergence                                        //( verify if any update messages queued to be sent)

								BGP Performance and Responsiveness:
								show version                                                   //( collect all before and after testing that show performance / responsive issue)
								show process location []
								show process threadname location []             //( difference of CPU times between two outputs to determine amount of work performed by each thread in the system)
								show bgp all all process performance-statistics detail                 //( lots of stats, timestamps, RIB info, afi , safi , messages, states )

								BGP Debugs: // (some debugs can consume CPU, reference to documentation and get customer approval before running debugs)
								dumpcore running [jid for bgp process] location []             //(  active/standby RP's  , recommended to get before escalation)
								debug bgp all                                                                        //(  All BGP debug)
								debug bgp ?                                                                         //( BMP Family , Communication library, Dampening if enabled, events, keepalive,
																																	Label, nexthop, policy-execution, postit, rpki, sync, table, update)
								debug bgp i?                                                                       //( BGP import processing, Choose a particular BGP instance AS, input/output)
								debug bgp rib                                                                      //(  BGP interaction with IP RIB)


								BGP Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								TechZone - IOSXR BGP Troubleshooting steps  > https://cloudsso.cisco.com/idp/startSSO.ping?PartnerSpId=https://techzone.cisco.com/auth/saml&redirectreason=notregistered&TARGET=https%3A%2F%2Ftechzone.cisco.com%2Ft5%2FASR-9000%2FIOS-XR-BGP-Troubleshooting-steps%2Fta-p%2F805366
								Techzone - Troubleshooting IOS XR BGP Common Problems >  https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Troubleshooting-IOS-XR-BGP-Common-Problems/ta-p/260738#anc6
								Techzone - BGP Troubleshooting Engineering Wiki > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/BGP-Troubleshooting-Engineering-Wiki/ta-p/892599#anc0
								Wiki - BGP Troubleshooting Information > http://wiki-eng.cisco.com/engwiki/BGP_20Troubleshooting_20Information
								Support - troubleshooting high cpu caused by the bgp scanner or bgp router process > http://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/107615-highcpu-bgp.html
								Jive- BGP Flags > https://cisco.jiveon.com/docs/DOC-66192
								IETF - RFC4271 - A Border Gateway Protocol 4 (BGP-4) > https://tools.ietf.org/html/rfc4271
								Cisco Tool - BGP Message Decoder > http://wwwin-routing.cisco.com/cgi-bin/bgp_decode/bgp_decode.pl
								cs-xr-bgp@cisco.com
								q-bgp-dev@cisco.com
								""",

							'BGP NSR': """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show running-config router bgp
								show bgp                                                                //( Non-stop routing is enabled)
								show bgp x.x.x.x/y detail standby                                       //(  lists the path received from active, active bestpath and best path calculated by standby)
								show bgp process performance-statistics | beg NSR         //( NSR state on active/standby, Most recent time stamp on state tell us state currently at)
								show bgp summary                                          //( look at standby ver)
								show bgp summary standby                                 //( steady-state should catch up with BGP main routing table version)
								show bgp neighbor x.x.x.x performance-statistics         //( NSR state of a neighbor and more NSR statistics)
								show tcp nsr br                                                               //( should see BGP session)
								show redundancy                                                      //( NSR is ready)
								show redundancy standby
								show bgp nsr                                                             //( NSR ready, NSR parameters)
								show bgp summary nsr standby                                //(  Summary information, states with timestamps)
								show bgp summary nsr                                              //( summary specific afi/safi. Shows entire state machine transitions  )
								show bgp sessions                                                     //( Neighbor address, VRF id, Spk AS #, InQ, OutQ, NBRState, NSRState )
								show bgp sessions not-nsr-ready
								show bgp sessions not-nsr-ready standby
								show bgp sessions                                                     //( BGP neighbors currently configured along with their peering state as well as NSR state)
								show bgp sessions not-established                            //( only list not established or not nsr ready )
								show dll jobid [ bgp_jid ]  location []
								show bgp table vpnv4 unicast                                    //(  neighbors associated with a given table (afi/safi))
								show bgp table vpnv4 unicast standby                       //(  prefixes synced from active to standby. PfxRcdif X and Y same then all synced from active )
								show tech routing bgp file [media:filename]
								show tech routing bgp nsr file [media:filename]

								show bgp trace sync reverse | inc "active NSR state"        //(  NSR state machine moves, current state and events that caused transitions in the states)
								debug bgp commlib                                                        //(  encoding/decoding between active/standby , brib/spkr etc)

								// BGP NSR Not Ready (If in TCP setup done, bgp is waiting for address family convergence. BGP will not start NSR unless all the neighbor has received the updates up to BGP nsr converge version)

								show redundancy                                          //( standby node is ready or not
								show running router bgp                               //( nsr is configured or not)
								show process bgp location                           //( running active standby and all threads are created)
								show bgp nsr [standby]                                //( shows partner endpoint with valid data)
								show bgp process perf  loaction                   //( active and standby global nsr state )
								show log | inc NSR terminated                      //(  too many re-transmissions for a neighbor, TCP sends an OPER_DOWN to active and standby BGP)
								show bgp sessions                                        //( sessions to be synced, active bgp is in TCP Init-Syn, waiting for one session to come up or waiting on TCP to complete TCP sync)
								show bgp all all converge                                         //( show all the address family configured for bgp)
								show bgp [afi] [safi] summary nsr                         //(  address family is NSR converged or not )
								show bgp [afi] [afi] summary nsr                           //( neighbor whose Ackver and or TblVer is less than BGP nsr converge version)
								show bgp vrf all [afi] [safi] summary nsr                //( vpnv4 or vpnv6 afi  check InQ or OutQ for a neighbor in pending or not)
								show tcp brief                                                            //(  neighbor data in the send/receive buffer or not)
								show bgp update-group neighbor x.x.x.x                  //( neighbor is in any update group )

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - BGP NSR Troubleshooting > http://wiki-eng.cisco.com/engwiki/BGP_20Troubleshooting_20Information#head-2c9ee8469d3e97f96e56288d16037a24eb28accb
								Wiki - IOXNRS/NRSTroubleshootingGuide > http://wiki-eng.cisco.com/engwiki/IOXNRS_2fNRSTroubleshootingGuide
								cs-xr-bgp@cisco.com

								""",

							'BGP Process': """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show bgp process                                                         //( status / summary information, variations for afi/safi , performance, details)
								show process location []                                             //( thread on node(s). Issue multiple times, determine where CPU resources are spent )
								show process blocked location []                                //( If consistently appearing may be a deadlock involving the BGP process)
								show placement program bgp                                      //( location where bgp is running, state, jid, group, standby state)
								show bgp [[afi] [safi]] process
								show bgp [[afi] [safi]] process detail                              //( memory usage statistics by important internal data structures)
								show bgp [[afi] [safi]] process performance-stat      //( real time spent performing operations, time stamps for states during initial convergence)
								show process distribution [process name]                   //( bpm, bgp, brib, to find the Job IDs (JID) of the various BGP processes that are running)
								show proc bgp location all                                              //( check the status of the BGP speaker processes)
								show proc brib location all                                              //( check the status of the bRIB processes)
								show proc bpm location all                                             //( check the status of the BPM process)
								show process [job ID] location []                                //( information about a specific process instance ( location omitted if running on the local node))
								show process threadname [job ID] location []            //( work performed by a particular thread and thread names for a process)
								show dll jobid [job ID] location []                                //( needed to decode tracebacks from the BGP process)
								top d location []                                                       //( monitors threads using CPU resources. list of processes at the top of the window)
																							//( To exit from top, use q or CTRL-C)

								BGP Debugs: // (some debugs can consume CPU, reference to documentation and get customer approval before running debugs)
								dumpcore running [jid for bgp process] location []             //(  active/standby RP's  , recommended to get before escalation)
								debug bgp all                                                                        //(  All BGP debug)
								debug bgp ?                                                                         //( BMP Family , Communication library, Dampening if enabled, events, keepalive,
																																	Label, nexthop, policy-execution, postit, rpki, sync, table, update)
								debug bgp i?                                                                       //( BGP import processing, Choose a particular BGP instance AS, input/output)
								debug bgp rib                                                                      //(  BGP interaction with IP RIB)

								BGP Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								TechZone - IOSXR BGP Troubleshooting steps  > https://cloudsso.cisco.com/idp/startSSO.ping?PartnerSpId=https://techzone.cisco.com/auth/saml&redirectreason=notregistered&TARGET=https%3A%2F%2Ftechzone.cisco.com%2Ft5%2FASR-9000%2FIOS-XR-BGP-Troubleshooting-steps%2Fta-p%2F805366
								Techzone - Troubleshooting IOS XR BGP Common Problems >  https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Troubleshooting-IOS-XR-BGP-Common-Problems/ta-p/260738#anc6
								Techzone - BGP Troubleshooting Engineering Wiki > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/BGP-Troubleshooting-Engineering-Wiki/ta-p/892599#anc0
								Wiki - BGP Troubleshooting Information > http://wiki-eng.cisco.com/engwiki/BGP_20Troubleshooting_20Information
								Support - troubleshooting high cpu caused by the bgp scanner or bgp router process > http://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/107615-highcpu-bgp.html
								Jive- BGP Flags > https://cisco.jiveon.com/docs/DOC-66192
								IETF - RFC4271 - A Border Gateway Protocol 4 (BGP-4) > https://tools.ietf.org/html/rfc4271
								Cisco Tool - BGP Message Decoder > http://wwwin-routing.cisco.com/cgi-bin/bgp_decode/bgp_decode.pl
								cs-xr-bgp@cisco.com
								q-bgp-dev@cisco.com
								""",

							'BGP VPNV4': """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show bgp vpnv4 unicast process perf
								show bgp vpnv4 unicast process detail
								show bgp vpnv4 unicast summary
								show bgp vpnv4 unicast rd [remote rd] x.x.x.x/y [detail]
								show bgp vpnv4 unicast nexthops x.x.x.x/y
								show bgp vpnv4 unicast labels
								show bgp vrf [vrfname to import] summary
								show bgp process location all
								show bgp all all convergence
								show bgp vrf [vrf name ] imported-routes | inc x.x.x.x
								show bgp vrf [vrf name][prefix] detail
								show route vrf [vrf name][prefix] detail
								show bgp vrf [vrf name]process performance-statistics detail
								show bgp vrf all all sum
								show bgp vrf all all sum | utility egrep ^[1-9]
								show bgp vrf [ vrf name ]process performance-statistics det | be Prefixes
								show bgp sessions
								show bgp sessions not-established
								show bgp vpnv4 unicast convergence

								show bgp trace location all

								BGP Debugs: // ( Some debugs can consume CPU, reference to documentation and get customer approval before running debugs)
								dumpcore running [jid for bgp process] location []             //(  active/standby RP's  , recommended to get before escalation)
								debug bgp all                                                   //(  All BGP debug)
								debug bgp ?                                                    //( BMP Family , Communication library, Dampening if enabled, events, keepalive,
																								Label, nexthop, policy-execution, postit, rpki, sync, table, update)
								debug bgp i?                                                   //( BGP import processing, Choose a particular BGP instance AS, input/output)
								debug bgp rib                                                  //(  BGP interaction with IP RIB)


								BGP Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								TechZone - IOSXR BGP Troubleshooting steps  > https://cloudsso.cisco.com/idp/startSSO.ping?PartnerSpId=https://techzone.cisco.com/auth/saml&redirectreason=notregistered&TARGET=https%3A%2F%2Ftechzone.cisco.com%2Ft5%2FASR-9000%2FIOS-XR-BGP-Troubleshooting-steps%2Fta-p%2F805366
								Techzone - Troubleshooting IOS XR BGP Common Problems >  https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Troubleshooting-IOS-XR-BGP-Common-Problems/ta-p/260738#anc6
								Techzone - BGP Troubleshooting Engineering Wiki > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/BGP-Troubleshooting-Engineering-Wiki/ta-p/892599#anc0
								Wiki - BGP Troubleshooting Information > http://wiki-eng.cisco.com/engwiki/BGP_20Troubleshooting_20Information
								Support - troubleshooting high cpu caused by the bgp scanner or bgp router process > http://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/107615-highcpu-bgp.html
								Jive- BGP Flags > https://cisco.jiveon.com/docs/DOC-66192
								IETF - RFC4271 - A Border Gateway Protocol 4 (BGP-4) > https://tools.ietf.org/html/rfc4271
								Cisco Tool - BGP Message Decoder > http://wwwin-routing.cisco.com/cgi-bin/bgp_decode/bgp_decode.pl
								cs-xr-bgp@cisco.com
								q-bgp-dev@cisco.com
								""",

							'CEF IPv4': """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show cef
								show cef [a.b.c.d]
								show cef location []
								show cef non-recursive
								show cef drop                                                           //(  repeat multiple of times )
								show cef unresolved location []
								show cef summary location []
								show cef resource det location []
								show cef adjacency [type] [interface] location []
								show cef interface [type] [interface] location []
								show cef exception location []
								show cef hardware [ ingress | egress ] location []
								show cef [a.b.c.d] [mask] internal
								show cef exact-route [src-ip] [dst-ip]
								show cef misc location []
								show cef ipv4 [a.b.c.d] detail
								show cef ipv4 [local addr a.b.c.d]  detail location []            //( collect on ingress and egress line cards )
								show cef ipv4 [remote addr a.b.c.d]  hardware [ ingress | egress ] detail location []      //( see link CEF+Troubleshooting for command details   )
								show cef ipv4 drop location []                                                                       //( repeat multiple of times )
								show cef ipv4 exceptions location []                                                             //( exception statistics , issue multiple times )
								show cef vrf [vrf-name] [prefix/length] hardware [ ingress | egress ] det location []
								show cef vrf traffic ipv4 [a.b.c.d] hardware [ ingress | egress ] location []
								show cef vrf all unresolved location []
								show adjacency
								show adjacency [type] [interface] location []
								show adjacency [type] [interface] remote detail location []                       //(  ipv4 adjacency, ifhandle)
								show adjacency [type] [interface] remote detail hardware location []       //( ingress line card , see link CEF+Troubleshooting for details)
								show adjacency summary
								show arp location []                                                                                       //( when L2 address needs to be checked)
								show tbm hardware afi-all unicast dual detail location [ node ]    //( displays tree bitmap hardware-related information)

								show tech-support cef
								show tech-support cef (ipv4, ipv6, mpls, vrf ) location [] file [ [media]:file_name ]

								show bcdl trace wrapping location [ node ]
								show cef mpls trace
								show cef platform trace all all location [ node ]          //( not supported on 12K)
								show adjacency trace all wrapping location [R/S/CPU0]
								show adjacency hardware trace wrapping location [R/S/CPU0]   //( not supported on 12K)
								show cef ipv4 trace loaction []
								show cef trace events
								show cef trace events location []

								debug ip cef drop  //(  Show packets being dropped by CEF)
								debug ip cef receive  //(  Show packets being received (punted to next switching layer)
								debug ip packet
								debug ip cef ipc     //( Turns on RP[-]LC IPC messages - can be very verbose)

								dumpcore running [jid] // ( jid for fib_mgr on the RP, use show process command)
								dumpcore running [jid] location [node] //(for fib_mgr on ingress and egress linecard, use show process fib_mgr location )

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - Troubleshooting CEF for IPv4 on the CRS-1 > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/q-tac/Troubleshooting/CEF/Troubleshooting_CEF_IPv4_on_CRS-1.html
								Wiki - CEF Troubleshooting > https://wiki.cisco.com/display/CFC/CEF+Troubleshooting
								Cisco Support - Cisco IOS XR Troubleshooting Guide for the Cisco XR 12000 Series Router > https://www.cisco.com/c/en/us/td/docs/routers/xr12000/software/xr12k_r3-9/troubleshooting/guide/tr39xr12kbook/tr39fwd.html
								Wiki - TCP-NSR-Socket Triage Page > https://wiki.cisco.com/display/SPRSG/TCP-NSR-Socket+Triage+Page
								Wiki - TCP Stateful SwitchOver (SSO) > https://wiki.cisco.com/pages/viewpage.action?pageId=23657845
								iox-ifc-dev@cisco.com
								""",
							'CEF IPv6': """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show ipv6 interface brief
								show ipv6 neighbors summary
								show ipv6 traffic brief

								show ipv6 trace [ io , ea, ma, nd, net ]

								CEF ipv6 related commands:
								show cef ipv6 summary location []
								show cef resource detail
								show cef ipv6 interface
								show cef ipv6
								show cef ipv6 summary
								show cef ipv6 exact-route [source prefix] [destination prefix] detail
								show cef ipv6 drops
								show cef ipv6 hardware [ ingress | egress ] detail
								show cef trace location all
								show cef platform trace ipv6 all location []
								show cef ipv6 trace location []

								BGP ipv6 related commands.:
								show bgp ipv6 all
								show bgp ipv6 unicast
								show bgp ipv6 unicast summary
								show bgp ipv6 unicast [prefix]
								show bgp ipv6 unicast neighbors
								show bgp ipv6 multicast
								show bgp ipv6 multicast summary
								show bgp ipv6 multicast neighbors
								show bgp ipv6 multicast advertised
								show bgp ipv6 multicast [prefix]

								OSPF ipv6 related commands.:
								show ospf ipv6 summary
								show ospf ipv6 routes
								show ospf ipv6 neighbor
								show ospf ipv6 interface [or Interface name]
								show ospf ipv6 [ospf area]
								show ospf ipv6 trace all

								Multicast forwarding ipv6 related commands.:
								show mfib ipv6 interface detail
								show mfib ipv6 interface [type][interface]
								show mfib ipv6 route detail
								show mfib ipv6 route *
								show mfib ipv6 route [prefix]
								show mfib ipv6 route summary
								show mfib ipv6 trace

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - IPv6 Neighbor Discovery > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/IOX_IO_Infrastructure/Triage%20Training/ND.ppt
								Wiki - IPv4/IPv6 MA/EA > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/IOX_IO_Infrastructure/Triage%20Training/ma_ea.ppt
								Wiki - TCP/UDP/RAW Triage > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/IOX_IO_Infrastructure/Triage%20Training/transports_triage.ppt
								Wiki - TCP-NSR-Socket Triage Page > https://wiki.cisco.com/display/SPRSG/TCP-NSR-Socket+Triage+Page
								Wiki - TCP Stateful SwitchOver (SSO) > https://wiki.cisco.com/pages/viewpage.action?pageId=23657845
								""",

							'Process Deadlock': """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show process blocked location all
								show proc [JID] location [] | inc "PID"
								follow process [PID ID] Iteration 5 location []        //( takes a snapshot of the process and produces a stack trace for each of its threads)
								follow job [job id] iteration 5 location []

								dumpcore running [JID | process name] location []

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - Essential Deadlock Information > http://wiki-eng.cisco.com/engwiki/Essential_20Deadlock_20Information
								""",

								'Disk/Filesystem':"""
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								admin install verify packages
								show pfm loc all                                                              //( Platform Fault Manager details of the linecards)
								show filesystem  location []                                                  //( verify if the filesystem is mounted)
								dir [media]:                                                                  //( verify if you can access the disk)
								show process blocked                                                          //(  look for processes such as hd_drv are blocked)
								show media
								show media trace error                                                        //( should be empty if there's no problems)
								show filesystem [bootflash]: all                                              //(  boot flashow memory layout and filesystem information)
																				//( Stale size; If this number is high filesystem will be doing lot of "reclaiming" activity to get free space)
																				//(  Flashow Lock Status ; show all the sectors that are locked)


								run chkfsys -uv /[media]:                                                  //( if there are any issues found, it will stop and ask if you want to fix the issue)
								run diskinfo -d [media]: -f                                                //( Checking firmware verison for flashow disks)
								#run diskinfo -d [disk0]: -v 1 (turn ON)                                  //( Turn ON/OFF flashow disk driver debugs ([disk0]: and disk1: only)
								#run diskinfo -d [disk0]: -v 0 (turn OFF)

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - Disk Mirroring/Partitioning Wiki > http://wiki-eng.cisco.com/engwiki/IOS_20XR_20Disk_20Partition_2fMirroring
								Wiki - FileSystem Tshoot Guide > http://wiki-eng.cisco.com/engwiki/Filesystem_20Troubleshooting_20Guide
								Techzone - Troubleshooting Filesystem and Physical Disk Issues > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Troubleshooting-Filesystem-and-Physical-Disk-Issues/ta-p/575334
								Techzone - Formatting disks from ROMMON > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Formatting-Disks-From-ROMMON/ta-p/484215
								""",

							'FIB': """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show cef misc                                //( statistics for CEF, protocol ( ipv4, ipv6, mpls, common, delete history, platform capabilities)
								show cef tables summary
								show cef internal
								show cef unresolved detail
								show cef vrf all
								show cef resource
								show cef trace
								show tech-suport cef [vrf xxx] [ipv4|ipv6|mpls] detail [location] [node]

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - IOXFORWARD/FIB triage diagnostics > https://wiki.cisco.com/display/IOXFORWARD/FIB+triage+diagnostics#FIBtriagediagnostics-BasicinformationneededforanyDDTSLISP
								Techzone - DEs IOS-XR FIB Collaborators  > https://techzone.cisco.com/t5/IOS-XR-PI-Forwarding-Infra-Eng/IOS-XR-FIB-Collaborators/ta-p/1087741

								asr9k-fib-triage ASR9K
								crs-l3fib-india CRS
								crs-l3fib-india NCS 6K
								fretta-fwd-dev NCS 5500
								skywarp-pd-sw NCS 5K
								sunstone-dev Sunstone
								""",

							'GSP': """
								Useful Commands For Troubleshooting:  //( Some commands syntax could vary according to platform or version)
								show health gsp
								show gsp memoryShow process blocked
								show gsp ens client [ PID]                                     //( ENS client process ID)

								show tech gsp
								show tech gsp client process  [ name ]                 //( where is name of client process of gsp that is having problem/delay)

								Dumpcore running gsp                                       //( Running Core of GSP on the same node on which process is blocked)
								Dumpcore running [jid of the process gsp is blocked on]     //(  Running Core of the process which is blocked on GSP)

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - GSP Trouble Shooting Guide > https://wiki.cisco.com/display/PII/GSP
								""",

							'POS/SONET/DWDM/cHDLC': """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								POS/Sonet:
								show controllers sonet [rack/slot/module/port]                                              //( check counters and power levels )
								show hw-module sub [rack/slot/module] status pluggable-optics [no]
								show controller pos [rack/slot/module/port]

								show sonet-local trace all location []
								or
								show sonet-local trace error location[]
								show sonet-local trace frr location[]
								show sonet-local trace info location[]
								show sonet-local trace init location[]
								show sonet-local trace periodic location[]
								show pos trace all location []


								cHDLC:
								show chdlc ma interface  [type] [location]          //( shows hdlc keepalive packets )
								show interface [ type] [ interface number ]
								show chdlc trace all location all

								debug chdlc ma slarp packets interface [type] [location]  [interface-name]
								show tech-support chdlc interface [ifname]
								show tech pfi

								DWDM:
								show controller dwdm [rack/slot/module/port]
								show controller dwdm [rack/slot/module/port] g709
								show controller dwdm [rack/slot/module/port] optics

								show controller tenGigE [rack/slot/module/port]
								show interface tenGigE [rack/slot/module/port]

								debug g709
								debug plim
								debug dwdm


								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Techzone - Channelized Interfaces Cheat Sheet > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Channelized-Interfaces-Cheat-Sheet/ta-p/114172
								Techzone SONET down because of PPLM Alarm: https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/ASR9K-IOS-XR-SONET-Controller-down-due-to-PPLM-Alarm/ta-p/474637
								Techzone - ASR9K IOS XR SONET Controller down due to PPLM Alarm  > https://techzone.cisco.com/cisco/attachments/cisco/xr_other@tkb/31/1/dwdm%20768%20npi.ppt
								Techzone - SONET and DWDM tshoot > https://techzone.cisco.com/cisco/attachments/cisco/xr_other@tkb/31/6/SONET-DWDM.ppt
								Techzone - POS tshoot > https://techzone.cisco.com/cisco/attachments/cisco/xr_other@tkb/31/7/sonet-pos.ppt
								Wiki - POS Troubleshooting > http://wiki-eng.cisco.com/engwiki/PosTroubleShooting
								Ask ASR9K Knowledge Base - Tshoot APS > http://asr9k.cisco.com/ask/index.php?action=artikel&cat=12&id=486&artlang=en
								Techzone - Understanding and Troubleshooting POS/SONET, DWDM, MR-APS Chalk Talk Part 1 & 2 > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Understanding-and-Troubleshooting-POS-SONET-DWDM-MR-APS-Chalk/ta-p/108208
								Wiki - CHDLC Intro > http://wiki-eng.cisco.com/engwiki/CHDLCIntro
								Wiki - CHDLC troubleshooting > http://wiki-eng.cisco.com/engwiki/CHDLCTroubleShooting
								Wiki CHDLC Triage Info > http://wiki-eng.cisco.com/engwiki/CHDLCTriageInfo
								q-dwdm-sw@cisco.com
								""",

							'CDS Context Distribution Service': """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show cds producer trace location all | file [tftp server/filename]          //(  Shows trace for producer )
								show cds consumer trace location all | file [tftp server/filename]
								show cds server trace | file [tftp server/filename]
								show cds proxy trace location all | file [tftp server/filename]

								debug cds server func                                       // ( enable on the active RP and capture the syslogs printed in next 5 minutes, and then disable)
								run pidin | grep cds

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - CDS wiki-Cisco > https://wiki.cisco.com/pages/viewpage.action?pageId=63732778
								q-cds-dev@cisco.com
								""",

							'ISSU': """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								check the status of ISSU process:
								admin show issu
								admin show install issu stage
								admin show install issu stage detail                                         //( to check the status of ISSU manager state machine)
								admin show install request                                                   //( to check the progress of install operatio)
								admin show install issu inventory
								admin show install issu inventory detail                                     //( to check the status of individual nodes)
								admin show issu-warm-reload detail

								admin show controllers fabric plane all
								admin show tech ISSU
								admin show tech install

								check iMDR progress: // not required during normal ISSU behavior
								show imdr trace all loc all
								show install issu inventory                                                 //( find out nodes failing during imdr window)
								show imdr stage current info location all                                   //( nodes failing during imdr window)
								show cef imdr loc []
								show cef platform trace all all loc []
								more [media]/tmp/sysmgr.log                                                //( from nodes not completing iMDR)
								more [media]/nvram:/sysmgr_nv.log                                          //( from nodes not completing iMDR or getting reloaded during iMDR )
								admin show epm trace issue loc []

								show tech pfi
								show tech fabric                                                             //( for CRS during load/fabric upgrade)

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Techzone - Understanding and Troubleshooting ISSU > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Understanding-and-Troubleshooting-ISSU/ta-p/620918
								Wiki - Getting to know ISSU > https://wiki.cisco.com/display/CRSISSU/Getting%20to%20know%20ISSU
								Wiki - ISSU Basic Debugging > https://wiki.cisco.com/display/CRSISSU/ISSU+Basic+Debugging
								crs-ism-dev
								a9k-ism-dev

								""",

							'MDR Minimum Disruption Restart': """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								admin show warm-reload location []                                             //( check current MDR status )
								admin show warm-reload detail location []                                    //( check historical MDR status)
								admin show warm-reload all location []                                         //( check each process's MDR status)
								admin show warm-reload all sigterm-not-returned location []        //( check the processes which didn't replied to SIGTERM from sysmgr)
								admin show warm-reload all sigkill-received location []                 //( check the processes which is killed by sysmgr)
								admin show warm-reload [Name or JobID] location []                 //( get only one specific process's information)

								show log | inc %OS-SYSMGR-5-NOTICE : Card is WARM started
								show proc boot loc []                                       //( verify that all the processes are running)
								show warm-reload loc []                                   //( check the output to make sure all processes are gracefully shutdown (using SIGTERM))
																						//( Note that, terminating any process by SIGKILL doesn't mean a failed MDR, but, should be)
																						//( brought to the attention of the component owner)
								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - IOX-MDR > http://wiki-eng.cisco.com/engwiki/IOX_2dMDR
								""",

							"REDCON Redundancy": """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								console log
								show redundancy
								show redundancy trace
								admin show pcds client REDCON dump CRITICAL 64 DUMPALL location []                    //( debug from PCDS )
								show process [proc name] location []               //(redcon client process which is in question ( both active and standby ) , If it is not running,  the redcon client can not sync its database between standby and active node. check why the redcon client is not running)
								standby not ready due to syncfs issue:

								show red detail                                    // if shows redcon is waiting on syncfs IO operation, run the following:
								show ltrace syncfs2 error
								show ltrace syncfs2 event
								show syncfs2 locklist
								show syncfs2 synclist

								sh_ltrace_syncfs2 -IEVS                          //( from AUX to list all ltrace messages)
								show cfgmgr trace location []                      //( Check whether startup configuration has been applied on the active RP_

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - Redcon > http://wiki-eng.cisco.com/engwiki/redcon
								Wiki - Standby "not ready" tshoot > http://wwwin-iox.cisco.com/wiki/doku.php/lighthouse:dinfra:debug:case1
								Wiki - Troubleshooting traffic loss on failover without NSR > http://wwwin-iox.cisco.com/wiki/doku.php/lighthouse:failover:debug:case1
								iox-pi-infro-triage@cisco.com
								""",

							'RSVP': """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show rsvp neighbor                                                                  //(  info about RSVP peering sessions with neighbor)
								show rsvp session                                                                    //(  info regarding RSVP enable sessions)
								show rsvp interface  [ type] [ interface number ]                  //( info about RSVP configured interface)
								show rsvp counter message summary                                     //( info about RSVP  drops or packet info in detail)
								show rsvp counter events                                                         //(  any drop or lost packet info regarding RSVP enable interface)
								show rsvp counters                                                                   //( rsvp enable interface packet counters)
								show rsvp coun messages summary                                        //(  rsvp enable interface packet counters in detail)
								show rsvp interface [ type] [ interface number ] detail          //(  rsvp enable pos interface info)
								show rsvp counters destroy-reasons                                        //( show reason of faulty or drop packets)
								show rsvp counters notifications-client                                      //( info to client about RSVP related counters)
								show rsvp interface private
								show rsvp sender                                                                      //( info about sender to rsvp packet)
								show rsvp sender detail                                                            //( detail info about sender)
								show run | inc rsvp|mpls traffic-eng tunnel
								show run rsvp
								show rsvp trace
								show tech mpls rsvp file [media]:filename                             //( info about MPLS traffic engineering enable RSVP terminal)
								debug rsvp

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - RSVP info and Troubleshooting  > http://wiki-eng.cisco.com/engwiki/RSVP_20information
								q-rsvp-dev@cisco.com

								""",

							'Shelfmgr': """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show reboot history reverse loc []
								show process blocked location [active RP]
								show process blocked location []
								show process shelfmgr-partner location [active RP]
								show process i2c_server location []
								show i2c trace common location [active RP]
								show i2c trace error location [active RP]
								admin show i2c trace common location [node-SP]
								admin show i2c trace error location [node-SP]
								admin show platform | i [node]
								admin show shelfmgr status
								admin show shelfmgr node-history location []
								admin show shelfmgr notif location []
								admin show shelfmgr gsp-notif location []
								admin show shelfmgr power location []
								admin show shelfmgr database [ ccb, fsmcb, ncb, plimcb ] location []           //(  Card, Node, PLIM Configuration )
								admin show shelfmgr hardware                                                 //( Card Hardware)
								admin show shelfmgr dcdc location []                                         //( Power Send/Receive)
								admin show shelfmgr hb-history location [node]                               //( Node HB History)

								show tech-support shelfmgr

								admin show shelfmgr-partner trace
								show shelfmgr trace [ error, boot, startup ]
								debug shelfmgr [ boot, startup, fsm ]

								Collect depending on relevance:
								show tech gsp
								show tech lrd
								admin show tech [ control-ethernet, invmgr, install ]
								admin show tech fabric fast-snapshot
								admin show tech fabric plane

								Other Related Shelfmgr CLIs:
								admin show cctl trace shelfmgr    //( only on RP/SC nodes
								admin show install trace mbimgr  //( only on RP/SC nodes
								admin show cetftp trace all           //( only on RP/SC nodes
								admin show cctl trace server        //( only on RP/SC nodes
								admin show i2c-ctrl trace common   //( only on RP/SC nodes
								admin show i2c-ctrl trace error          //( only on RP/SC nodes
								show gt-i2c trace                             //( only on RP/SC nodes
								show gt-i2c trace error                   //( only on RP/SC nodes

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - Reading Shelf Manager trace > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/q-tac/Troubleshooting/BOOT/reading_shelfmgr_trace.html
								Techzone - Understanding and Troubleshooting > https://techzone.cisco.com/t5/CRS-Carrier-Routing-System/Understanding-and-Troubleshooting-Shelf-Manager/ta-p/194274#TimeoutA
								Wiki - Shelf Manager Debug  > http://viking-twiki1/twiki/bin/view/Viking/ShelfMgrDebug
								""",

							'SHMWIN':"""
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show shmwin summary location []                                            //( will give you how much in use and free memory on a node)
								show memory heap dllname  [jid]                                             //( groups memory blocks by allocator PC, sorts by size)
								show watchdog trace | i high water mark                                    //( look for continuous increase in high water mark for a suspected processes )
								show shmwin ifc-mpls list all location []                                    //( Will give ifc process location and meory size)
								show shmwin ifc-mpls list alloc location []                                //( show icp mpls memory size)
								show shmwin ifc-mpls list free location []                                  //( show amount of free memory and location where its free)
								show shmwin ifc-mpls list recyc location []                               //( show location where recycle memory is located)
								show shmwin ifc-mpls malloc-stats location []                          //( show memory allocation and stats of used memory)
								show shmwin ifc-mpls pool all-pools location []                        //( show total size of memory available and pools)
								show watchdog threshold memory configured location []    //(Wdsysmon monitors how much free memory there is on each node)

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - IOS XR Shmwin Wiki >	http://wiki-eng.cisco.com/engwiki/IOS_20XR_20Shmwin_20Wiki
								""",

							'SNMP': """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show snmp                                                                     //( information about SNMP process)
								show snmp mib statistics                                               //(  snmp polling stats, max timestamp per object and average time stamp calculation)
								show snmp mib access                                                  //( display a list of MIB module object identifiers (OIDs) registered on the system )
								show snmp mib access time                                          //( list of MIB module object identifiers (OIDs) registered on the system, with appropriate time)
								show snmp mib dll
								show snmp mib object-name
								show snmp mib | i  [ mibid  ]                                        //( search for mib  example; 1.3.6.1.4.1.9.9.221)
								show snmp mib ifmib general                                        //(  ifmib cache hit/miss couners - helps with performance analysis)
								show snmp mib ifmib cache                                           //(   displays time value for cache retrieval last 500 entries)
								show snmp queue rx                                                      //( show transmit of SNMP)
								show snmp sub-agent                                                    //( After polling agents receiving polling give there info)
								show snmp sub-agent group [ ? ]                                   //(  Agents receiving polling interface info)
								show snmp request drop summary                                //( Give drop packets info and size)
								show snmp request pending-queue detail                     //( shows the request tipe, id, source of request and timestamp it hit the queue)
								show snmp request type summary                                //( displays stat for snmp PDU types per NMS (max 30 unique NMSs)
								show snmp request type detail                                      //( similar but reformatted output to show snmp queue statistics incoming)
								show snmp request incoming-queue detail                   //( shows queue depth and processing counts per NMS)
								show snmp request overload stats                                //( display overload statistics for traps)
								show snmp request drop detail                                      //( request in requests queue must be processed within 10sec, or dropped. Count is drops per agen)
								show snmp queue statistics incoming                           //( shows customer snmp management stations and stats)
								show snmp queue statistics processing                        //( shows processing counts per sub agent, drops due to internal AIPC failures between snmpd | mibd)
								show snmp statistics oid group [ ? ]                              //(  dissects the internal processing time to MIB times, from MIB times, AIPC)
								show snmp statistics pdu                                              //(  further expands on per in NMS internal stats)
								show snmp traps                                                      //(  enhances existing command to show sent,drops,retries. Displays up to 50 trap objects per host)
								show snmp oid slow stats
								show snmp oid poll stats                                             //(  per object counts per NMS)
								show process block                                                   //(  for snmp process blocked , issue 5 times)
								run top_procs -D                                                   //( wait 1 minutes, then Ctrl+c exit)
								show process snmpd
								show process sysdb_mc
								follow process [pid snmpd]
								follow process [pid snmpd] delay 1 iteration 60
								show process memory [jid snmpd]
								show process sysdb_mc
								follow process [pid sysdb_mc] delay 1 iteration 60
								show process memory [jid sysdb_mc]
								show memory heap summary [jid sysdb_mc]
								show memory heap summary [jid snmpd]
								show sysdb connections shared-plane
								show sysdb statistics clients last 5 shared-plane

								show statsd requests detail
								show udp brief                                              //( look at the queue size)
								show lpts pifib hardware police loc []
								show memory summary bytes location all
								show watchdog overload state location []                    //( watch dog traces and memory on LC or RSP)

								show tech snmp [location]                                             //( complete show tech of snmp process, can specify location)
								show tech-support snmp ifmib                                       //( just for snmp ifmib process)


								Debugs Trace:
								show snmp trace lib group infra mibmgr error | inc Mempoolmib                                 //( snmp mibmgr process info)
								show snmp trace requests                                                                      //(  show device request for SNMP trace)
								show watchdog trace
								show snmp trace timeout                                                                      //(  value of snmp trace remove time out)
								show snmp trace slow oid location all                                                         //(  snmp polling information)
								show snmp trace overload                                                                     //( shows what snmpd is doing with the notifications)
								show sysdb trace [ edm, access, connection, edm, medusa, request, response, verification ] shared-plane tailf

								dumpcore running snmp

								debug snmp [ packet, request, lib ]
								debug snmp mib enhancedmempoolmib
								debug snmp general
								debug snmp lib object request

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - SNMP_TROUBLESHOOTING > https://wiki.cisco.com/display/XRSNMP/SNMP_TROUBLESHOOTING
								Wiki - IOS-XR SNMP Triage > https://wiki.cisco.com/display/XRSNMP/IOS-XR+SNMP+Triage
								Techzone - SNMP fails to respond to request due to overload control > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Solution-SNMP-fails-to-respond-to-request-due-to-overload/ta-p/80168
								Wiki - snmpd blocked on sysdb_mc here > http://wiki-eng.cisco.com/engwiki/snmpd_20blocked_20on_20sysdb_5fmc
								Wiki - StatsDebugging > http://wiki-eng.cisco.com/engwiki/StatsDebugging
								Cisco Support - IOS XR SNMP Best Practices>	http://www.cisco.com/c/en/us/td/docs/ios_xr_sw/iosxr_r3-9-1/mib/guide/crs-gsr_appe.html
								Support Forums - ASR9000/XR: Understanding SNMP and troubleshooting > https://supportforums.cisco.com/document/132706/asr9000xr-understanding-snmp-and-troubleshooting
								Techzone - SNMP Overview, Configurations & Troubleshooting on XR  > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/SNMP-Overview-Configurations-amp-Troubleshooting-on-XR/ta-p/832784
								Cisco tool- SNMP Object Navigator >	http://tools.cisco.com/Support/SNMP/do/BrowseOID.do?local=en
								q-snmp-dev@cisco.com

								Cisco  Support - ASR9K MIB Specification Guide > http://www.cisco.com/en/US/docs/routers/asr9000/mib/guide/asr9kmib3.html
								""",

							'SONET': """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show controllers sonet [ sonet line number]  all
								show controllers sonET [ sonet line number]  framers
								show controllers sonET [ sonet line number] internal-state
								show plim plaspa trace all location []
								show sonet-local trace all location []
								show sonet-local trace error location []
								show sonet-local trace frr location []
								show sonet-local trace info location []
								show sonet-local trace init location []
								show sonet-local trace periodic location []
								show pos trace all location []
								show controllers pos [ pos interface number]
								show controllers pos [ pos interface number] all

								show tech-support pos

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Cisco  Support - Troubleshooting PSE and NSE Events on POS Interfaces > http://www.cisco.com/en/US/tech/tk482/tk607/technologies_tech_note09186a008009464b.shtml
								""",

							'XFP SFP CPAK': """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show controllers [ interface type] [interface numer] all
								show hw-module subslot [subslot numer] status pluggable-optics
								show hw-module subslot [subslot numer] brief pluggable-optics
								show hw-module subslot [subslot numer] ltrace spa
								show hw-module subslot [subslot numer] ltrace mac

								show plim ether trace info location []
								show plim ether trace err location []
								show plim plim-ether trace all all location []                           //( works for 14-10GbE does not work for 4-10GbE)
								show plim xge-plim trace all loc []

								show ether-ctrl [ Gig | tengig | management ] trace all location []
								show ether-ctrl  [ Gig | tengig | management ] trace all verbose location []

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Cisco Support - Cisco 10-Gigabit Ethernet Transceiver Modules Compatibility Matrix : http://www.cisco.com/c/en/us/td/docs/interfaces_modules/transceiver_modules/compatibility/matrix/10GE_Tx_Matrix.html
								CRS PLIM: crs-plim@cisco.com, codc-crs-plim@cisco.com
								""",

							'SPP Software Packet Path': """
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show spp node location []
								show spp interface location []
								show spp graph
								show spp client location []
								show spp node-counters location []

								clear spp node-counters
								clear spp interface
								clear spp client

								show spp sid stats location []                            //( To know how many SID have been received for / injected by clients)
								show spp buffer location []


								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Viking - What is SPP > http://viking-twiki1/twiki/bin/view/Viking/SppDebug
								Viking - SPP Debug > http://viking-twiki1/twiki/bin/view/Viking/SPPDebug
								Viking - TRoubleshooting Viking Puntinject > http://viking-twiki1/twiki/bin/view/Viking/TroubleshootingVikingPuntInject
								Techzone - ASR9000 punt and inject path troubleshooting > https://techzone.cisco.com/t5/ASR-9000/Troubleshooting-Guide-ASR9000-PUNT-AND-INJECT-PATH/ta-p/242728
								Techzone - Debugging RSP punts and injects on ASR9000 using SPP user interface > https://techzone.cisco.com/t5/ASR-9000/Debugging-RSP-punts-and-injects-on-ASR9000-using-SPP-user/ta-p/48432
								Wiki - SPP Nodes > http://enwiki.cisco.com/SPP/Nodes
								Wiki SPP troubleshooting > http://enwiki.cisco.com/InterfaceManager/TroubleShooting/Data
								Wiki - InterfaceManagerFAQ > http://enwiki.cisco.com/InterfaceManager/FAQ
								Wiki - XR Packet Memory Leak > http://tac-wiki.cisco.com/XR_Packet_Memory_Leak
								Cisco Support - Process Memory Management commands on IOS XR > http://www.cisco.com/en/US/docs/routers/crs/software/crs_r4.0/system_management/command/reference/b_yr40crs_chapter_01011.html#wp1283995789
								Wiki - Packet Capturing at SPP > https://wiki.cisco.com/display/PUNTERS/Packet%20Capturing%20at%20SPP
								Techzone - SPP packet Capture on ASR9K > https://techzone.cisco.com/t5/ASR-9000/SPP-packet-Capture-on-ASR9K/ta-p/566308
								""",


							'Telnet/SSH/Console':"""
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show tcp brief
								show tcp trace
								show process devc-vty detail
								show process devc-conaux detail
								show lpts bindings brief location[] | inc any.23                      //(location is that the interface you want to telnet belongs to)
								show line trace vty 0 {error , slow}
								show line trace console slow
								show tty trace {info , error , warning}  all all

								SSH:
								show ssh
								show sshow session details

								debug sshow server
								debug sshow client
								debug sshow kex
								debug crypto pki errors
								debug crypto pki messages


								telnet
								show cinetd services
								debug telnet detailed
								debug cinetd                      //(Try telnet while debug cinetd is turned on, see if any message shows up. If not, please consult TCP)

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - IOX Telnet > http://wiki-eng.cisco.com/engwiki/IOX_2dtelnet
								Wiki - IOX TTY  > http://wiki-eng.cisco.com/engwiki/IOX_2dTTY
								Techzone - Loss management access > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/lost-of-managment-access-to-XR-device-telnet-ssh-console/ta-p/350822
								Techzone - Common SSH Syslog Messages in IOS XR > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Common-SSH-Syslog-Messages-in-IOS-XR/ta-p/776538
								iox-sec-dev@cisco.com
								""",

							'Statsd Infrastructure':"""
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show statsd manager info
								show statsd collectors brief location [] { jid [job ID]}
								show statsd requests
								show statsd requests errors
								show statsd summary
								show statsd performance

								show gsp group name statsd_global_group location          //( members of the stats group , All collectors should be a member of this group)
								show gsp group name statsd_mgr_global_group location []   //( Only the stats manager is a member of this group. All collectors should be writers to it)

								show statsd manager trace
								show statsd performance trace
								show statsd server trace

								debug statsd manager error
								debug statsd manager sysdb-edm

								show tech statsd
								show tech gsp

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - StatsDebugging > http://wiki-eng.cisco.com/engwiki/StatsDebugging
								""",

							'STP Spanninbg Tree':"""
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show spanning-tree vlan [vlan name] detail
								show spanning-tree interface
								show spanning-tree trace controller
								show spanning-tree [ blockedports | inconsistentports | pathcost method ]
								show spanning-tree summary
								show spanning-tree bridge
								show spanning-tree active
								debug spanning-tree packet raw rec int [type] [interface number]

								MSTP:
								show spanning-tree mst
								debug spanning-tree mst controller all
								debug spanning-tree mst io all location [problem_node]
								show tech spanning-tree mst [name]

								show spanning-tree mst id trace controller verbose
								show spanning-tree mst id trace io verbose location []

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - MSTP Troubleshooting > http://enwiki.cisco.com/MSTP/MSTP/Troubleshooting
								Wiki - Essential Debug Information > http://enwiki.cisco.com/MSTP/Troubleshooting/EssentialInformation
								Wiki - MSTPTroubleshootingMSTPCrashes > http://enwiki.cisco.com/MSTP/Troubleshooting/MSTPCrashes

								iox-mstp-dev@cisco.com
								""",

							'SVD Selective VRF Download':"""
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)

								show run | in selective-vrf-download                       //( is it configured)
								show svd role                                                          //( track SVD  roles )
								show svd state []                                                   //( track SVD  states)
								show rsi state [ location [] ]                                    //( Card Roles, Interface counts, card operational SVD state)
								show rsi role-transitions [ location [] ]                     //( rsi state changes )
								show rsi clients type producer location []
								show rsi table ipv[4|6] [unicast] location []
								show cef tables location []                                   //( CEF table downloaded to a given location.)
								show cef tables [detail/summary]                          //( displays total number of routes(local/remote) , R flag for SVD remote )
								show rsi table vrf [vrf-name] ipv4 collocation      //(  Info about rsi table configured with vrf)
								show rib tables selective-vrf-download

								show trace rsi
								show cef trace svd
								debug rsi [ agent | lib | adync-lib | master ]


								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - SVD (Selective VRF Download) config , debug and TS > https://wiki.cisco.com/pages/viewpage.action?pageId=7301453
								Wiki - SVD > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/SVD/
								xr-svd-dev
								""",

							'Sysdb':"""
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show processes exec detail location all

								show sysdb statistics advanced location []
								show sysdb statistics client [client job id]
								show sysdb statistics client [client job id] shared-plane-nc
								show sysdb connections job [jid] shared-plane
								show sysdb registrations verification job [jid] shared-plane
								show sysdb medusa registrations edm location []
								show health sysdbclear sysdb statistics shared-plane-nc

								Install:
								admin show tech install
								admin show install log rev det

								PFI/IM:
								show tech pfi
								show im history system
								show im database verbose interface [interface name] location []

								show tech-support cfgmgr
								show tech-support sysdb
								show tech-support rdsfs

								show sysdb trace (other options}
								dumpcore running syslogd location []

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Cisco support - Sysdb Triage Help > http://wwwin-people.cisco.com/kkataria/material/sysdb.html
								Wiki - SysDB > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/SysDB-wiki/ta-p/894912
								Wiki -IOS SysDB >  http://wiki-eng.cisco.com/engwiki/IOXSysDB
								Wiki - IOXSysDB/SysDBBasics > http://wiki-eng.cisco.com/engwiki/IOXSysDB_2fSysDBBasics
								Wiki - IOXSysDB/SysDBTroubleshootingGuide > http://wiki-eng.cisco.com/engwiki/IOXSysDB_2fSysDBTroubleshootingGuide
								Techzone - Using sysdbcon to trigger temperature alarm (and snmp trap) > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Using-sysdbcon-to-trigger-temperature-alarm-and-snmp-trap/ta-p/63208
								Techzone - Introduction to sysDB and Troubleshooting sysDB > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Introduction-to-sysDB-and-Troubleshooting-sysDB/ta-p/658346
								q-sysdb-dev@cisco.com
								""",

							'Syslog':"""
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show logging
								admin show logging
								show run logging                                   //( provide info on configured logging settings)
								show syslog trace self [slow/self]
								Complete Console logs
								show logging output                             //( show the status of the logging count facility (Count and time-stamp logging messages))
								show process syslogd

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - IOX-SYSLOG > http://wiki-eng.cisco.com/engwiki/IOX_2dSYSLOG
								""",


							'TACACS':"""
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
								show run tacacs source-interface [type] [ interface number ]
								show proc tacacsd
								show tacacs
								show tacacs requests
								show tacacs server-groups
								show tacacs trace

								debug tacacs
								debug tacacs [authentication/authorization/accounting]


								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Cisco Doc - Configuring AAA Services on Cisco IOS XR Software > https://www.cisco.com/c/en/us/td/docs/ios_xr_sw/iosxr_r3-2/security/configuration/guide/sc_c32/sc32aaa.pdf
								""",


							'TCP':"""
								Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)

								General:
								show tcp brief                                                          //( Brief listing of all TCP sockets/connections, pcb address)
								show tcp detail pcb [value from tcp brief]                            //( info for a specific socket or all sockets )
								show tcp counter state [state]                                         //(  count of all connections in a specific [state])
								show tcp packet-trace [ PCB value ]                                   //(  details for send/rcv packets info for a tcp connection)
								show tcp stat sum
								show tcp statistics
								show tcp statistics pcb [pcb_no or all ]  location []            //( service tcp-keepalives-in service tcp-keepalives-out)
								show tcp detail
								show tcp extended-filters
								show tcp extended-filters peer-filters location []                //(  Displays the LPTS filters)

								NSR:
								show tcp nsr brief
								show tcp nsr client brief location []
								show tcp nsr detail client
								show tcp nsr detail pcb [pcb address]                                   //( NSR state of tcp connection)
								show tcp nsr detail session-set [ [SSCB] | all ] [location ]     //( session-set, time when initial-sync was initiated)
								show tcp nsr session-set brief                                                 //( how many sessions by bgp to replicated, successfully replicated)
								show tcp nsr statistics client [ [CCB] | all ] [ location ]           //( interaction between nsr (client) and the TCP stack)
								show tcp nsr statistics session-set [ [SSCB] | all ] [ location ]   //(  operations on a session-)
								show tcp nsr statistics pcb [ [PCB] | all ] [ location ]              //(  Tx / Rx paths for a given session)
								show tcp nsr statistics summary [location ]                                 //( aggregate of all the statistics presented by the above command)

								show tcp trace
								show socket trace process tcp
								show tcp dump-list x.x.x.x                                                         //( list of files for a peer which has flapped/reset)
								show tcp dump-file all location []                                             //(  details for send/rcv packets info for a reset tcp connection)
								show tech-support tcp nsr                                             //( Collects tcp nsr tech support info)

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								External - rfc793 > http://www.tcpipguide.com/free/t_TCPOverviewHistoryandStandards-3.htm
								External - TCP Operational Overview and the TCP Finite State Machine (FSM) > http://www.tcpipguide.com/free/t_TCPOperationalOverviewandtheTCPFiniteStateMachineF-2.htm
								ioxsup@cisco.com
								q-tcp-dev@cisco.com
								"""
                        ,
		                'BCDL':"""
							    Useful Commands for Troubleshooting: //( Some commands syntax could vary from one platform to another)
							    sh bcdl                                                                          //  (group related info (currently just subgroup 0 for each bcdl group)
							    sh bcdl consumers                                                                //  (all consumers should reply, check error counter)
							    sh bcdl table
							    sh bcdl trace wra rev location [] file  media:[file-name]                       // (Data captures running debug of bcdl operation)
							    sh tech-support bcdl                                                            // (Data captures all-in-one command for all bcdl groups)

							    Reference Links:
							    BCDL Commands on Cisco IOS XR Software > https://www.cisco.com/c/en/us/td/docs/routers/xr12000/software/xr12k_r3-9/system_management/command/reference/yr39xr12k_chapter2.html
							    Cisco Doc-center - bcdl_2.0 > http://wwwin-eng.cisco.com/Eng/OIBU/IOS_XR_PI/Presentations/bcdl_exec.ppt
							    Cisco Doc-center  - BCDL methodology > http://wwwin-eng.cisco.com/Eng/OIBU/IOS_XR_PI/Presentations/bcdl_methodology.ppt
							    Wiki - Triage > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/IOX_IO_Infrastructure/Triage%20Training/BCDL_triage.ppt
							    Wiki - BCDL Debugging  > http://wiki-eng.cisco.com/engwiki/BCDL
						        """
                        ,
                        'BCDLv2':"""
								Useful Commands for Troubleshooting: //( Some commands syntax could vary from one platform to another)
								show bcdlv2  [ bcdl_group ]  update-groups [tabular]     // ( Shows list of current update groups and GSP multicast groups/consumers associated with it )
								show bcdlv2 [ bcdl_group ] consumer-view consumers all // ( Shows the stats on the consumer side )
								show bcdlv2  [ bcdl_group ]  ug-filters // (  Shows the ug to table mapping )
								show bcdlv2 [ bcdl_group ]  trace location [ ]
								show rib [ ipv6/ipv4 ] update-groups  // ( check for any issues of fib missing some ipv4/v6 prefixes and check for any frozen update groups issue multiple times with 60 sec. interval )

								Show Techs:
								show tech bcdlv2 [ bcdls_ipv4_rib, bcdls_ipv6_rib, bcdls_ipv4_lsd, bcdls_ipv6_lsd ]
								show tech [ rib, cef, gsp ]

								Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki - BCDL > https://wiki.cisco.com/display/IOXFORWARD/BCDLv2%20Triaging
								q-bcdl-dev@cisco.com
                                """
			            ,
						'XML/MDA':"""
								Useful Commands For Troubleshooting:  //( Some commands syntax could vary according to platform or version)
								show management xml trace
								show management xml tty trace
								show management xml mda trace
								show management xml client trace
								sh mda [connections | files | objects | trace ]

								Debugs:
								debug management xml mda verbose
								debug mda [errors][sysdb]

								Show Techs:
								show tech sysdb,
								show tech parser
								show tech cfgmgr

								Support links:  //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
								Wiki -XML/MDA Troubleshooting Information > http://wiki-eng.cisco.com/engwiki/XML_20and_20MDA_20Troubleshooting_20Information
								Techzone - Connecting to XML dedicated agent within an EnXR environment using TCP proxy > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/IOS-XR-XML-Connecting-to-XML-dedicated-agent-within-an-EnXR/ta-p/898351
								Techzone -IOS XR XML: Troubleshooting > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/IOS-XR-XML-Troubleshooting/ta-p/898378
								q-mda-dev@cisco.com Email alias to reach the XML/MDA development team.
								q-schema-police@cisco.com Email alias to send schema change requests for your component
                                """
          }

dict_ASR9K = {
                'ABF': """ // (ACL Based Forwarding)
                    Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show access-list ipv4 [acl_name] hardware ingress location []       //( Verify ABF is programmed correctly in the hardware with right next hop )
					show controllers np counters all location []                        //( Check if there are any global ucode counters for ABF )
					show qoshal app-queue client irb np [] location []                  //( Check which TM loopback queue packets are sent to )
					show pfilter-ea ha chkpt region all location []                     //( Provides the checkpoint record info and pfilter-ea state )

					Debugs:
					debug ipv4 access-list dll all location []
					debug pfilter-ea abf location []

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - Introduction AFB > http://viking-twiki1/twiki/bin/view/Viking/ABF#Introduction
					Cisco Support Forum - ASR9000/XR ABF (ACL Based Forwarding) > https://supportforums.cisco.com/t5/service-providers-documents/asr9000-xr-abf-acl-based-forwarding/ta-p/3153403
					Wiki - ABF White Paper > ABF white paper http://wwwin-eng.cisco.com/Eng/ERBU/ABF_white_paper.docx
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
   					viking-pbr@cisco.com
                    asr9k-abf@cisco.com
					cs-asr9k@cisco.com
                   """,

				'ACL':"""
                    Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show access-lists ipv4                                                  // (Displays the list of ace configured for access-list)
					show access-lists ipv4 summary
					show access-lists ipv4 [acl] hardware [ingress | egress]              // (Displays the tcam entries for access-list)
					show access-lists ipv4 [acl] hardware [ingress | egress] resource-usage loc {location}     // (shows compiled ACL hardware stats (TCAM, compression, etc))
					show access-lists maximum detail
					show access-lists usage pfilter location []                                       // ( Displays the interfaces using the access-list )
					show access-list ethernet-service                                                 // ( Displays the aces of configured access-list )
					show access-list ipv4 trace
					show access-list ethernet-services trace
					show prm server trace error loc []      // (PRM ( platform resource manager) , controls hw programming between CPU / NPU and attached asics/memory )
					show prm server trace init loc []
					show prm server tcam summary all ACL [np#] location []              //  (shows the ACL tcam summary output)
					show prm server tcam summary all all [np#] location []              //  (Displays the tcam utilization for all features (like ACL, QOS, IFIB))
					show pfilter-ea fea summary location []                           // (shows pfilter_ea np resource consumption)
					show pfilter-ea fea ipv4-acl [ACL] location []                     // (shows you how many ACEs, how many TCAM entries, and TCAM entries per ACE)
					show pfilter-ea bundle                                               // (Displays the requisite information for a bundle interface)
					show access-lists usage pfilter location []                          //(shows interfaces which have an ACL and which ACL is applied)
					show pfilter-ea ipv4 trace critical all location  []
					show pfilter-ea ipv4 trace intermittent all location  []
					show controller np ports all location  []        // ( Checking NP Used by which interfaces )

                    Debugs:
                    debug pfilter-ea all
					debug pfilter-ea detail
					debug pfilter-ea errors
					debug pfilter-ea info
					debug pfilter-ea range
					debug pfilter-ea trace
					debug pfilter-ea vmr

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					TechZone - ASR9000 ASR9K TCAM Utilization (Access-list, ACL, etc) > https://techzone.cisco.com/t5/ASR-9000/ASR9000-ASR9K-TCAM-Utilization-Access-list-ACL-etc/ta-p/647586
					Wiki - Viking ACL TOI's > https://wiki.cisco.com/display/HEROBU/ACL#ACL-CiscoWikiLink
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					q-acl@cisco.com
					""",

				'Bundle LACP':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					All bundles:
					sh bundle                                                                                                  // (Display operational information for bundle interfaces)
					sh bundle brief                                                                                          // (Display information about all bundles in a tabular format)
					sh bundle load-balancing [bundle] [detail] location [node]                 // (Display information used for bundle load-balancing)
					sh bundle load-balancing brief location [node]                                    // (Display a summary of the load-balancing information for all bundles)
					sh bundle protect [bundle]                                                                   // (Display operational information from the bundle protect database in a user friendly format)
					sh bundle scheduled-actions [bundle]                                                  //(Display any actions scheduled to take place on a bundle at some point in the future)
					sh bundle status                                                                                        // (Verify the sanity of the current bundle configuration and the health of the software)
					sh bundle trace all location [LC]
					sh bundle trace process adj loc [LC]

					LACP:
					sh lacp [[bundle]/[member]]                                                                   // (Display a detailed view of the LACP parameters of ports within a bundle)
					sh lacp counters [[bundle]/[member]]                                                    // (Display the counters of 802.3ad packets sent and received)
					sh lacp counters unaccounted [node]                                                      // ((Display packet drops on unknown/non-LACP/LACP-inactive ports)
					sh lacp packet-capture [decoded] [in/out] [member interface]                 //( Display captured LACP and marker packets)
					sh lacp system-id                                                                                       // (Display the LACP system id used for the global LACP system)
					sh lacp system-id (all/iccp-group [number])                                             // (Display the LACP system id(s) used for all LACP systems)

					mLACP:
					sh mlacp [iccp-group [number]] [brief/verbose]                                      // (Display the state of mLACP redundancy groups and nodes, bundles and ports within them)
					sh mlacp counters [(ig/bdl/mbr)-info] [[IG/bundle/member]]                   //( Display counters for mLACP TLVs sent and received)
					sh mlacp inconsistencies                                                                          // (Display any inconsistencies and misconfigurations in the mLACP setup)
					sh mlacp tlv-capture ([bundle]/raw) (in/out)                                           // ( Display captured mLACP TLVs)

					Internal commands:
					sh bundle infrastructure counters bfd [[bundle/member]]                                                                                     // (Display BFD state transition statistics)
					sh bundle infrastructure database [ma/ea] [global/(ig/bdl/local-node/mbr)-info] [[IG/bundle/node/member]]       // (Database dump for one or more bundle processes)
					sh bundle infrastructure database protect [[bundle]]                                                                                             // (Display BM-Distrib protect thread database)
					sh bundle infrastructure ea [[bundle]] [detail]                                                                                                        // (Display BM-EA internal state)
					sh bundle infrastructure event [(ig/bdl/mbr)-info] [[IG/bundle/member]]                                                                // (Displays events in the bundle infra)
					sh bundle infrastructure in-progress [ma/ea] [(ig/bdl/mbr)-info] [[IG/bundle/member]] [brief]           // (Display async operations in progress / pending operation retries)
					sh bundle infrastructure lacp-io [[bundle/member]]                                                                             // (Display BM-Local shared memory database dump)
					sh bundle infrastructure mac-allocation                                                                                         //  (Display unused MAC addresses allocated to BM-Distrib by EMA)

					sh tech-support bundles

					debug lacp packet ...

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - IOS XR Bundle Infra > http://wwwin-ensoft.cisco.com/enwiki/BundleInterfaces  (PI)
					Wiki - Bundle Interface Show Commands > http://enwiki.cisco.com/BundleInterfaces/ShowCommands
					Cisco Support Forum - Troubleshooting Guide: IOS XR Bundles > https://supportforums.cisco.com/document/143711/troubleshooting-guide-ios-xr-bundles
					Wiki - Link Aggregation Control Protocol > http://enwiki.cisco.com/BundleInterfaces/LACP
					TechZone - Bundle down due to LACPPDU packets loss > https://techzone.cisco.com/t5/ASR-9000/Bundle-down-due-to-LACPPDU-packets-loss/ta-p/802059
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					iox-lb-dev@cisco.com
					viking-protection@cisco.com  (Bundle PD)
                    """,

				'Console & AUX':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show line
					show line [aux| console |vty] location []
					show line trace [aux | console | vty] error
					show line trace [aux | console | vty] slow
					show line trace [aux | console | vty] fast
					show line [aux | console | vty] location []
					show line statistics [aux | console | vty] device                               //(TTY Port HW Buffer Statistics)
					show line statistics [aux | console | vty] end-to-end                           //(TTY Port End To End Buffer Stats)
					show line statistics [aux | console | vty] flow-control
					show line statistics [aux | console | vty] iochar
					show line statistics [aux | console | vty] datapath
					show line  statistics [aux | console | vty] end-to-end
					show tty trace info all all location all
					show tty trace error all all location all

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Cisco Docs - Command Reference > https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/asr9k-r6-2/sysman/command/reference/b-system-management-cr-asr9000-62x/b-sysman-cr-asr9k-61x_chapter_010110.html#wp1635156802
                    TechZone - New RSP440 Cards having console problem > https://techzone.cisco.com/t5/IOS-XR-PI-OS-Infra-Eng/SR-682502369-New-RSP440-Cards-having-console-problem-BEMS643223/td-p/1077082
                    TechZone - Aux port generating Noise > https://techzone.cisco.com/t5/ASR-9000/631266645-Aux-port-generating-Noise-over-30-ASR9Ks/td-p/711603
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					q-tty-dev@cisco.com
					""",

				'Control Ethernet EOBC':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show controllers backplane ethernet brief location [node-id ]                             // (To display brief information about backplane Ethernet interfaces in a particular location)
					show controllers backplane ethernet links location [Active RSP]
					show controllers backplane ethernet switch link all loc [Active RSP]
					show controllers backplane ethernet switch link all loc [Standby RSP]
					show controllers backplane ethernet detail location [LC]
					show controllers backplane ethernet detail location [Active RSP]
					show controllers backplane ethernet detail location [Standby RSP]
					show controllers backplane ethernet manageability interface all location all

					show tech-support control-ethernet
					//(For more details on troubleshooting EOBC please refer to link in reference (ASR9K EOBC Trouble Shooting Guide )

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Cisco Jive - ASR9000 EOBC explanation > ASR9000 EOBC explanation : https://cisco.jiveon.com/docs/DOC-1544244
					Cisco Jive - ASR9K EOBC Trouble Shooting Guide > https://cisco.jiveon.com/docs/DOC-1787721
					Cisco Jive - EOBC High Level Debubbing Tips > https://cisco.jiveon.com/docs/DOC-1787721#jive_content_id_EOBC_High_Level_Debugging_Tips
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					""",

				'DHCP Proxy':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					sh dhcp ipv4 proxy binding
					sh dhcp ipv4 proxy interface []
					sh dhcp ipv4 proxy profile na proxy location []
					sh dhcp ipv4 proxy statistics location []     // (for all VRFs)
					sh dhcp vrf default ipv4 proxy statistics interface gigabitEthernet 0/0/0/12.20
					sh dhcp ipv4 proxy statistics raw location []
					sh dhcp ipv4 proxy binding detail location []
					sh dhcp ipv4 proxy binding summary location []

					Debug and Trace Commands:
					sh dhcp ipv4 trace proxy
					debug dhcp ipv4 proxy internals
					debug dhcp ipv4 proxy []
					debug dhcp ipv4   // (this is more useful and more informative command)

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Cisco Support Forum - ASR9000/XR Understanding DHCP relay, proxy and forwarding broadcasts > https://supportforums.cisco.com/docs/DOC-15933
					Wiki - DHCP Snooping Troubleshooting > https://wiki.cisco.com/display/SPRSG/DHCPv4+Snoop+Troubleshooting
					TechZone - DHCP Snooping troubleshooting > https://techzone.cisco.com/t5/ASR-9000/ASR9k-DHCP-snooping-troubleshooting/ta-p/550469
					TechZone - DHCP Troubleshooting PROXY > https://techzone.cisco.com/t5/ASR-9000/DHCP-Troubleshooting-PROXY-on-ASR9000-with-IOS-XR/ta-p/798890?srnumber=682918063&app=MWZ&origin=RKI_Suggested
					Cisco Docs - Implementing the Dynamic Host Configuration Protocol > http://www.cisco.com/en/US/docs/routers/asr9000/software/asr9k_r4.0/addr_serv/configuration/guide/b_ic40asr9kbook_chapter_0100.html
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					iox-dhcp-support@cisco.com
					iox-dhcp-dev@cisco.com
					""",

				'DHCP Relay':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					sh dhcp vrf [vrf_name] ipv4 relay statistics
					sh dhcp ipv4 relay statistics                         // (DHCP packets received/transmitted by the DHCP Relay application on the RSP)
					sh dhcp ipv4 relay profile

					Additional checks:
					sh udp statistics pcb all                             // (Verify that the UDP application is receiving/transmitting packets on the RSP)
					sh netio client                                       // (Verify that NETIO is transmitting packets to UDP on the RSP)

					Traces:
					sh dhcp ipv4 trace
					show dhcp ipv4 trace relay events
					show dhcp ipv4 trace errors
					show dhcp ipv4 trace events
					show dhcp ipv4 trace packets
					show dhcp ipv4 trace internals

					Debugs:
					dhcpd relay all
					dhcpd relay errors
					dhcpd relay events
					dhcpd relay internals
					dhcpd errors
					dhcpd events
					dhcpd packet

					show Techs:
					show tech dhcp ipv4 snoop / relay
					show tech-support dhcp ipv4 relay vrf-name file
					show tech-support dhcp ipv4 relay profile-name file

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Cisco Support Forum - ASR9000/XR Understanding DHCP relay, proxy and forwarding broadcasts > https://supportforums.cisco.com/docs/DOC-15933
					Wiki - DHCP Snooping Troubleshooting > https://wiki.cisco.com/display/SPRSG/DHCPv4+Snoop+Troubleshooting
					TechZone - DHCP Snooping troubleshooting > https://techzone.cisco.com/t5/ASR-9000/ASR9k-DHCP-snooping-troubleshooting/ta-p/550469
					TechZone - DHCP Troubleshooting PROXY > https://techzone.cisco.com/t5/ASR-9000/DHCP-Troubleshooting-PROXY-on-ASR9000-with-IOS-XR/ta-p/798890?srnumber=682918063&app=MWZ&origin=RKI_Suggested
					Cisco Docs - Implementing the Dynamic Host Configuration Protocol > http://www.cisco.com/en/US/docs/routers/asr9000/software/asr9k_r4.0/addr_serv/configuration/guide/b_ic40asr9kbook_chapter_0100.html
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					iox-dhcp-support@cisco.com
					iox-dhcp-dev@cisco.com
					""",

				'DHCP Snooping':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					sh dhcp ipv4 snoop binding                                   //( Basic commands to see the status of the clients )
					sh dhcp ipv4 snoop binding mac-address                       //( Detailed info about a particular client )
					sh dhcp ipv4 snoop statistics                                //( High level stats with Tx, Rx and drop counters per bridge domain )
					sh dhcp ipv4 snoop statistics bridge-domain                  //( Per DHCP packet type drops counters, more granular )
					sh dhcp ipv4 snoop statistics raw                            //( summary display for all the bridge domains )
					show dhcp ipv4 snoop profile

    				run xipc_show -j [dhcpd jobid] -i 1 // to check the amount of data in the DHCPd queue

					Debug/Traces/Show techs:
					debug dhcp ipv4 packet filter-id mac-address                 // (This is a debug per MAC address introduced in 4.3.0)
					//(Caution:CSCue43007 Not able to disable dhcp packet debug at high packet rate integrated in 4.3.1 onwards.)

					sh dhcp ipv4 trace
					show dhcp ipv4 trace snoop errors
					show dhcp ipv4 trace snoop events
					show dhcp ipv4 trace snoop internals
					show dhcp ipv4 trace errors
					show dhcp ipv4 trace events
					show dhcp ipv4 trace packets
					show dhcp ipv4 trace internals

					show tech-support dhcp ipv4 snoop bridge-domain-name file
					show tech-support dhcp ipv4 snoop profile-name file

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Cisco Support Forum - ASR9000/XR Understanding DHCP relay, proxy and forwarding broadcasts > https://supportforums.cisco.com/docs/DOC-15933
					Wiki - DHCP Snooping Troubleshooting > https://wiki.cisco.com/display/SPRSG/DHCPv4+Snoop+Troubleshooting
					TechZone - DHCP Snooping troubleshooting > https://techzone.cisco.com/t5/ASR-9000/ASR9k-DHCP-snooping-troubleshooting/ta-p/550469
					TechZone - DHCP Troubleshooting PROXY > https://techzone.cisco.com/t5/ASR-9000/DHCP-Troubleshooting-PROXY-on-ASR9000-with-IOS-XR/ta-p/798890?srnumber=682918063&app=MWZ&origin=RKI_Suggested
					Cisco Docs - Implementing the Dynamic Host Configuration Protocol > http://www.cisco.com/en/US/docs/routers/asr9000/software/asr9k_r4.0/addr_serv/configuration/guide/b_ic40asr9kbook_chapter_0100.html
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					iox-dhcp-support@cisco.com
					iox-dhcp-dev@cisco.com

					""",

				'Base Commands':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show version
					show log
					show install log
					show aps
					show redundancy
					show context
					show environment all
					show run
					show configuration commit list
					show proc blocked location all
					admin show configuration commit list
					admin show install active sum
					admin show platform
					admin show inventory chassis
					admin show inventory
					admin show diag
					admin show hw-module fpd location all
					admin show reboot history location []
					admin show sysldr trace all location[]    //  (to see trace for specific LC)


					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - IOS-XR Troubleshooting Main Page > https://wiki.cisco.com/display/GSRTR/IOS-XR
					TechZone - XR OS and Platforms > https://techzone.cisco.com/t5/XR-OS-and-Platforms/ct-p/xr
					Cisco Jive - ASR9k Addition Links > https://cisco.jiveon.com/docs/DOC-245271
					XRGeeks - XR Geeks Page > http://xrgeeks.cisco.com/
                    TechZone - ASR9922 Troubleshooting reference > https://techzone.cisco.com/t5/ASR-9000/ASR9922-Troubleshooting-Guide/ta-p/708649?attachment-id=46739
					Cisco Jive - XR PI/PD DE Alias > https://cisco.jiveon.com/docs/DOC-619180
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					""",

				'Interfaces':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					sh controllers [tenGigE | gige]  [] internal
					sh controllers [tenGe | Gig] [] location [] phy                         // (This command shows the SFP/XFP EEPROM contents)
					sh controllers tenGigE [] xgxs                                          // (shows the XGXS information)
					sh controllers tenGigE [] mac
					sh controllers tenGige [] regs                                          //(shows the MAC registers)
					sh controllers [tenGigE |Gig] [] stats

					sh tech-support ethernet interface [tenGe |Gig] []

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Ask ASR9K Knowledge Base - Copper SFP support > http://asr9k.cisco.com/ask/index.php?action=artikel&cat=1&id=271&artlang=en
					Ask ASR9K Knowledge Base - Understanding PLATFORM-XFP-2-LOW_TX_POWER_ALARM > http://asr9k.cisco.com/ask/index.php?action=artikel&cat=12&id=378&artlang=en
					Ask ASR9K Knowledge Base - Tshoot 100GE interface down > http://asr9k.cisco.com/ask/index.php?action=artikel&cat=12&id=679&artlang=en
					Ask ASR9K Knowledge Base - Autonegotiation details > http://asr9k.cisco.com/ask/index.php?action=artikel&cat=12&id=684&artlang=en
					Ask ASR9K Knowledge Base - Carrier-delay details > http://asr9k.cisco.com/ask/index.php?action=artikel&cat=6&id=675&artlang=en
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					""",

				'Drops':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show interfaces
					show controller [interface]
					show controller np ports all location [LC]                                             // (Find out which interface maps to which NP)
					show drop location [LC]
					show qoshal default-queue subslot 0 port                                              //(output provides more details about the ingress and egress queues)
					show controller fabric fia stat location 0/RSP0/CPU0
					show controller fabric fia stat location [LC]

					Ingress NP:
					show controllers np counters [np_id] location []

					Ingress NP fabric counters:
					Show controllers np fabric-counters tx [np_id] location []

					Ingress bridge:
					show controllers fabric fia bridge stats location []

					Ingress FIA:
					show controllers fabric fia stats location []
					show controllers fabric fia drops ingress location[]
					show controllers fabric fia q-depth location []

					Ingress crossbar:
					show controllers fabric crossbar statistics instance 0 location []
					show controllers fabric crossbar statistics instance 1 location []

					Clear counters:
					clear counters all
					clear controller np counters all
					clear controller fabric fia location
					clear controller fabric crossbar-counters location

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					TechZone - Debugging packet drops > https://techzone.cisco.com/t5/ASR-9000/Debugging-packet-drops/ta-p/944514
                    Cisco Support Forum - Troubleshooting packet drops and understanding np counters > https://supportforums.cisco.com/document/59721/asr9000xr-troubleshooting-packet-drops-and-understanding-np-drop-counters
                    TechZone - Troubleshoot the interface output drops on ASR9K Trident line-card > https://techzone.cisco.com/t5/ASR-9000/How-to-Troubleshoot-the-interface-output-drops-on-ASR9K-Trident/ta-p/432421
                    Cisco Support Forum - Debugging input drops > https://supportforums.cisco.com/document/12098621/debugging-input-drops
                    Cisco Support Forum - NP Counters explained up to 4.2.1 > https://supportforums.cisco.com/document/110671/asr9000xr-np-counters-explained-xr421
                    TechZone - NP Typhoon counters > https://techzone.cisco.com/t5/ASR-9000/NP-Typhoon-counters/ta-p/299854
                    Cisco Support Forum - How to Capture dropped or lost packets > https://supportforums.cisco.com/document/122386/asr9000xr-how-capture-dropped-or-lost-packets
                    Cisco Support Forum - Capture dropped packets Typhoon NPs with "monitor np counter" command > https://techzone.cisco.com/t5/ASR-9000/Capture-Dropped-packets-on-A9SR9000-Typhoon-NPs-with-quot/ta-p/159696
                    Cisco Support Forum - Drops for unrecognized upper-level protocol error > https://supportforums.cisco.com/document/59521/asr9000xr-drops-unrecognized-upper-level-protocol-error
                    Ask ASR9K Knowledge Base - Debugging unrecognized upper-level protocol > http://asr9k.cisco.com/ask/index.php?action=artikel&cat=1&id=40&artlang=en
                    TechZone - SPP packet Capture on ASR9K > https://techzone.cisco.com/t5/ASR-9000/SPP-packet-Capture-on-ASR9K/ta-p/566308
                    TechZone - Platform CLI for SPP packet capture > https://techzone.cisco.com/t5/ASR-9000/Platform-CLI-for-SPP-packet-capture/ta-p/564354
                    TechZone - Debugging RSP punts and injects on ASR9000 using SPP user interface > https://techzone.cisco.com/t5/ASR-9000/Debugging-RSP-punts-and-injects-on-ASR9000-using-SPP-user/ta-p/48432
					Ask ASR9K Knowledge Base - Capture dropped packets with dbgtrace (hardcore!) > http://asr9k.cisco.com/ask/index.php?action=artikel&cat=12&id=474&artlang=en
					TechZone - Punt path packet capture (netio) > https://techzone.cisco.com/t5/ASR-9000/ASR9K-Punt-path-packet-capture-netio/ta-p/44686
					TechZone - Troubleshooting netio arp taildrop > https://techzone.cisco.com/t5/ASR-9000/Troubleshooting-netio-arp-taildrop/ta-p/164926
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					""",

                'Ethernet':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show controller tengig 0/s/0/p internal
					show controller tengig 0/s/0/p all
					show ethernet infra internal ea global                                                     // ( shows general ether-ea PI init & bind with PD info )
					show ethernet infra internal ea subs                                                     //( shows PI info (no PD) for features controlled by vlan_ea process )
					show ethernet infra internal ea trunks                                                   // ( shows PI info (no PD) for features controlled by ether_caps_ea process)

					Traces/debugs:
					show controllers vic ltrace all location []
					show prm server trace internal                                                             //(Display traces of internal event for Platform NP Manager)
					show ether-ctrl tengig trace all location []                                       // (Show all ethernet traces data)
					show ether-ctrl tengig trace all verbose location []
					show ether-ctrl tengig ltrace all location []
					show ethernet trace verbose loc []
					show ethernet driver trace location []                                            //  (Show internal trace logs for the Ethernet driver infrastructure)
					show ethernet infra trace                                                                     // (show trace outputs for ether_caps_ea and vlan_ea PI and PD )
					show ethernet infra trace [vertical-bar] include EAP                           // (filtered output gives PD traces only, ether_caps_ea & vlan_ea )
					debug ethernet infra ea all                                                                    //(Turn on all debugs, both PI and PD)
					debug etherea-lib infra all                                                                     //(Turn on debugs for ether ea PD dll (vkg_ether_ea_client_api.c))

					show tech-support ethernet                                                              //(dump & package all ether-ea debugging info)
					show tech-support ethernet interfaces
					show tech-support ethernet interfaces location []

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Ask ASR9K Knowledge Base - Unknown Mac/flooding packet path : http://asr9k.cisco.com/ask/index.php?action=artikel&cat=1&id=530&artlang=en
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					""",

              'Fabric':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					General Fabric:
					sh log | inc fabric
					sh controllers np
					sh controllers np summary all
					sh drops

					Fabric:
					sh controllers fabric fia                                                                       //  (FIA and Bridge FPGA)
					sh controllers fabric fia link-status location []                                   //  (describes the status of the links from the FIA to each fabric chip on the RSP)
					sh controllers fabric fia stats                                                              // (FIA (Octopus) issue multiple times)
					sh controllers fabric fia stats location []
					sh controllers fabric fia errors [ ingress | egress ] loc []
					sh controllers fabric fia drops [ ingress | egress ] loc[]
					sh controllers fabric fia bridge stats loc []                                        //  (bridge statistics for uni/multicast to/from each NPs the bridge serves, separate HP/LP Queue)
					sh controllers fabric fia bridge ddr-status location []                        // (used to find the link status between the bridge and octopus, issue multiple times)
					sh controllers fabric fia bridge sync-status loc []                             // (link sync status from bridge 0 and 1 to each NP that it serves)
					sh controllers fabric fia bridge flow-control loc []                             // (under congestion, can provide back pressure from the NP to bridge/fia and ingress linecards)
					sh controllers fabric fia q-depth location []
					sh controllers fabric crossbar link-status instance [ 0| 1 ] location []       // (active RSP )
					sh controllers np drvlog location[]                                                     //  (NP persistent init error message)
					sh controllers np portmap all location []                                            //  (NP ports mapping)
					sh controllers np counters all location []                                            // (issue multiple times  )
					sh controllers np ports all
					sh controllers np fabric-counters all all                                                // (issue multiple times  )

					Asic:
					sh asic-errors all detail location []
					sh asic-errors crossbar [ 0 | 1 ] all location [RSP]
					sh asic-errors fia [fia instance] all location []
					sh controllers fabric fia trace
					sh controllers fabric ltrace crossbar
					sh prm server trace error loc []
					sh controllers fabric arbiter ltrace location []
					sh tech fabric

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - ASR9K Fabric Overview and Troubleshooting Resources > https://wiki.cisco.com/display/HEROBU/ASR9K+Fabric+Overview+and+Troubleshooting+Resources
					Cisco Docs - Troubleshooting Fabric > https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/asr9k_r4-0/troubleshooting/guide/tr40asr9kbook/tr40fab.html
					Cisco Support Forum - ASR9000/XR: Understanding the Fabric and troubleshooting commands > https://supportforums.cisco.com/t5/service-providers-documents/asr9000-xr-understanding-the-fabric-and-troubleshooting-commands/ta-p/3147083
					TechZone - Troubleshooting fabric FIA tail drop on ASR9k > https://techzone.cisco.com/t5/ASR-9000/Troubleshooting-fabric-FIA-tail-drop-on-ASR9k/ta-p/935264
					TechZone - Punt Fabric Data Path Failures Troubleshoot Guide > https://techzone.cisco.com/t5/ASR-9000/ASR-9000-Series-Punt-Fabric-Data-Path-Failures-Troubleshoot/ta-p/426337
					TechZone - Troubleshooting ASR9K Fabric Issues > https://techzone.cisco.com/t5/ASR-9000/Troubleshooting-ASR9K-Fabric-Issues/ta-p/230436/message-revision/230436%3A2 https://techzone.cisco.com/t5/ASR-9000/Debugging-packet-drops/ta-p/944514
					Wiki - Debugging Viking Fabric Issues > http://ptlm-linux1/twiki/bin/view/Viking/VikingDebuggingFabricIssues
					Wiki - VIKING SWITCH FABRIC > http://viking-twiki1/twiki/bin/view/Viking/Fabric
					Wiki - Debugging Viking Fabric Issues > http://viking-twiki1/twiki/bin/view/Viking/VikingDebuggingXmenFabricIssues
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					viking-fabric-dev@cisco.com
					as9k-fabric-mgid@cisco.com
					""",

				'FAN Tray':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					admin show hw-module fpd location all                                // ( Displays the current FPD image versions, upgrade FPD image if needed)
					admin show diag [ fan location 0 | 1 ] detail
					admin show diag [ fan location 0 | 1 ] eeprom-info             // ( Displays field diagnostics results from the EEPROM)
					admin show environment all
					admin show environment table
					admin show environment leds
					show log events buffer bistate                                           // (  for the presence / non-presence of the Outstanding environmental condition report)
					admin show canbus server-stats loc all                             // ( repeat 2,3,4 times about 10-15 seconds apart)
					admin show canbus trace all location 0/FT1/SP
					admin show canbus trace all location 0/FT0/SP
					show proc | i canbus
					admin show environment trace
					show pfm trace location all                                                 // ( Displays the Platform Fault Manager traces)

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					TechZone - Setting Fan RPMs on the ASR 9010 > https://techzone.cisco.com/t5/ASR-9000/Setting-Fan-RPMs-on-the-ASR-9010/ta-p/764117
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
				    cs-asr9k@cisco.com
					""",
				'Filesystem':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show mirror
					show mirror loc all
					show media
					show filesystem
					show redunduncy
					show file [media]:
					show file [media]: stats
					admin show active-fcd location all
					fsck [ media]:

					show rdsfs trace error
					show rdsfs trace internal
					show rdsfs trace iofunc

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Cisco Docs - Filsystem Facts >http://wwwin-eng.cisco.com/Eng/OIBU/Q/SW_Reviews/filesystem_faq.txt@5
					Wiki - Filesystem Troubleshooting Guide > http://wiki-eng.cisco.com/engwiki/Filesystem_20Troubleshooting_20Guide
					Cisco Stg-Tools - Working with Filesystems > http://wwwin-stg-east.cisco.com/stg-tools/qnx/product/neutrino/user_guide/fsystems.html
					Cisoc Jive - ASR9K TURBOBOOT  >  https://cisco.jiveon.com/docs/DOC-1807535
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					""",

				'GRE Tunnel':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show tunnel ip ma database tunnel-ip [id]
					show uidb data location [] tunnel-ip [id] [ egress | ingress ]
					show adjacency tunnel-ip [id] internal detail
					show adjacency tunnel-ip [id] detail hardware
					show adjacency tunnel-ip [id] remote detail hardware
					show controllers np struct GRE-Encap all
					show controllers np struct GRE-QUAL all
					show controllers np counters all                                 // ( issue multiple times)
					show interface tunnel-ip [id]
					show cef drops                                                          // ( Look for GRE lookup drops and GRE processing drops)
					show tunnel ip trace netio all
					show tunnel ip platform trace all location
					show tunnel ip ma database all

					show tech-support tunnel-ip

					PI Debug commands:
					debug tunnel ip ma all    // ( Enable all Control/Management plane debugs)
					debug  tunnel ip ma trace
					debug tunnel ip ea all  // ( Enable all forwarding plane debugs)
					debug  tunnel ip ea trace
					debug tunnel ip netio all    // ( Enable debugs for slow path packet)
					debug  tunnel ip netio trace

					PD Debug commands:
					debug tunnel ip platform all   // ( Enable debugs for ASR9k h/w programming)

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					TechZone - Multipoint GRE implementation > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/XR-Multipoint-GRE-implementation/ta-p/770521
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					ox-tunnel-dev@cisco.com
					""",

				'HSRP VRRP':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show hsrp brief
					show hsrp [grp name/number] stat
					show l2vpn
					show controllers [interface] all
					show vrrp interface [grp name/number] statistics                   // ( Display brief status of all vrrp interfaces)
					show lpts pifib hardware entry statistics location []                // ( Verify that the packets are coming into the router, by checking the hardware statistics)
					show lpts pifib hardware police location []                           // ( If drops, verify the policer values against the incoming traffic)
					show ethernet driver internal all driver-id all location []

					show tech-support vrrp
					show tech-support hsrp

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - HSRP/VRRP Homepage > http://enwiki.cisco.com/FHRP
					Wiki - HSRP / VRRP FAQs > http://enwiki.cisco.com/FHRP/FAQ
					Wiki - HSRP / VRRP Intro > http://enwiki.cisco.com/FHRP/Intro
					Wiki - HSRP / VRRP Troubleshooting > http://enwiki.cisco.com/FHRP/Troubleshooting
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					xr-hsrp-vrrp-support@cisco.com
					""",

				'ISM':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					admin show platform summary location []                                 // ( Should be compatible SW version)
					admin show install active summary
					admin show diagnostic result location []

					show cgn nat44 [Service_interface_name] statistics
					show services interfaces
					show interfaces serviceinfra 1
					show interface serviceapp * accounting
					show services role detail
					show services interfaces

					show cgn trace services errors
					show cgn nat44 demo inside-translation protocol tcp inside-vrf Inside inside-address  [ip address] port start  [start port] end [end port]
					show cgn demo outside-translation protocol tcp outside-vrf Outside outside-address  [ip address] port start  [start port] end [end port]
					show cgn demo pool-utilization inside-vrf Inside address-range [start ip][end ip]

					Take the following logs 3 times with a gap of one minute each:
					show controllers np counters all location [LC]      // ( for inside and outside non-ISM LC )
					show controllers fabric fia stats location [LC]       // ( for inside and outside non-ISM LC )
					show controllers np fabric-counters all all location [LC]             // ( for inside and outside non-ISM LC )
					show controllers fabric fia stats location [ISM]
					show interfaces serviceapp * accounting
					show interfaces serviceapp *
					show spp interface location [ISM]                        // ( Show Software Packet Path interface statistics (RX/TX/CTX))
					show spp node-counters location [ISM] show drops np all

					show tech-support services cgn
					show tech-support service-module all location [loc]

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - CGv6 on ISM: Trouble-Shooting Guide Installation and Configuration > https://wiki.cisco.com/display/WPRVSM/CGv6-ISM-TSG-Config
					Wiki - CGv6 on ISM: Trouble-Shooting Guide > https://wiki.cisco.com/display/WPRVSM/CGv6-ISM-TSG
					Wiki - ISM Project Wiki > https://wiki.cisco.com/display/WPRVSM/CGv6-ISM
					Wiki - CGv6 on ISM Deployment > https://wiki.cisco.com/display/WPRVSM/CGv6-ISM-Deployment
					TechZone - ASR9k ISM: To get 10Gbps throughtput with 2 different inside vrf and one outside vrf > https://techzone.cisco.com/t5/ASR-9000/ASR9k-ISM-To-get-10Gbps-throughtput-with-2-different-inside-vrf/ta-p/453803
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					cgn_avsm@cisco.com
					""",

				'L2VPN':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show mpls ldp neighbor [neighbor address ] detail                            // ( client AToM LDP may be UP but PW down if PW is not configured on another end)
					show l2vpn xconnect
					show l2vpn xconnect  detail                                                  // ( UP, MTU, CW, traffic details)
					show l2vpn forwarding location []                                            // ( should be UP)
					show l2vpn forwarding detail location []                                      // ( If Seg2 / 1 is unbound issue between L2FIB and L3FIB/L2TP)
					// ( if the Seg1 is unbound and Seg 2 is bound, issue between L2FIB and AIB
					show l2vpn bridge-domain
					show l2vpn bridge-domain br
					show l2vpn bridge-domain detail
					show l2vpn pw-class  de
					show mpls forwarding
					show l2vpn forwarding summary location []                                         // ( look for dropped messages)
					show l2vpn trace reverse                                                                       // ( search for error )
					show l2vpn platform trace all all
					show l2vpn atom-db detail
					show l2vpn forwarding bridge-domain mac-address loc []
					show l2vpn forwarding int [ interface type] [ interface number ] det location []                                                  // ( Counters for Tx and Rx issue multiple times)
					show l2vpn forwarding int [ interface type] [ interface number ] hardware ingress debug detail location []             // ( HW programming)
					show mpls forwarding labels [label] hardware egress detail deb location []            // ( Hardware path check. Adjacency should be valid only on egress)

					show tech-support l2vpn
					show tech-support l2vpn platform
					show l2vpn trace

					Debugs:
					Xconnect not coming UP:
					debug l2vpn ac
					debug mpls ldp pw server
					debug mpls ldp pw sig
					debug l2vpn atom api

					FWD related Issues:
					debug l2vpn forwarding ens
					debug l2vpn forwarding aib
					debug l2vpn forwarding netio
					debug l2vpn forwarding table xc
					debug l2vpn forwarding table nh


    				Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - IOS-XR L2VPN Triage > https://wiki.cisco.com/display/XRL2VPN/IOS-XR%20L2VPN%20Triage
					Wiki - XR L2VPN Main Web Page > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/XR-L2VPN/
					TechZone - L2VPN VPLS. Troubleshooting > https://techzone.cisco.com/t5/ASR-9000/asr9000-L2VPN-VPLS-Troubleshooting/ta-p/890794
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					viking-l2-sw@cisco.com
					l2vpn-xr-support@cisco.com
					evpn-xr-support-tool@cisco.com
					""",

				'LC Crash':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show filesystem                                                // ( Check got files related to same timestamp of the crashow  )
					dir [media]:/dumper location                                 // ( Check both active and standby for related files)
					dir [ media]:/np
					dir [ media]:/sysmgr_debug/                                  // ( Look for files created with the name starting debug.node0_0_CPU0 and timestamp)
					more [ media]:/sysmgr_debug/debug.node0_0_CPU0.XXXXXX        // ( collect related files and attach to SR)
					show reboot history location []
					show reboot last syslog location []
					show reboot last crashow location []
					admin show logging onboard uptime location[]
					admin show logging onboard cbc dump-all location []
					admin show logging onboard cbc most-recent loc []

					show asic-errors all location []
					show controllers np soft-errors all all location []
					show controllers np interrupts all all location []
					show prm stats summary location []
					show prm server trace [ error , event, hal, internal, init ] location []

					admin show logging onboard cbc dump-all location [rsp active, stb, lc ]                    // ( Display all OBFL records for Can Bus Controller (cbc))
					admin show logging onboard error all location [rsp active, stb, lc ]                       // ( Display the onboard failure logging (OBFL) error messages)
					admin show logging onboard uptime location [rsp active, stb, lc ]

					show cli history detail
					admin show shelfmgr trace

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					""",

				'LC Boot':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					admin show cetftp ipaddr [ip address tftp server ]                                    // (IP address of platform control plane TFTP server if used)
					show controllers np drvlog location []
					show controllers backplane ethernet detail location []                                  // ( issue multiple times )
					admin show logging onboard cbc dump-all location []                                  // ( can take 2-3 mins)
					admin show diagnostic trace rev loc []
					show reboot history location []
					show reboot last syslog location []
					show pfm location []
					show log location []
					admin show diag location []
					admin show diagnostic result location [] detail
					dir /recurse [media]: location all

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - ASR9K Micro Image FAQ > http://ptlm-linux1/twiki/bin/view/Viking/MicroImageFaq
					Wiki - ASR9K Archive Restore > http://ptlm-linux1/twiki/bin/view/Viking/ArchiveRestore
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					""",

				'Licences':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					admin show license
					admin show license evaluation
					admin show license log operational
					admin show license log administration
					admin show license udi
					admin show license status
					admin show license file
					admin show license features
					admin show license traces
					admin show tech-support license
					admin show diag chassis
					dir [media]:/license location [active / stby RSP ]

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					ASR 9000 License storage clean up > https://techzone.cisco.com/t5/ASR-9000/ASR-9000-License-storage-clean-up/ta-p/179010
					Wiki - IOS XR Entitlement > http://wiki-eng.cisco.com/engwiki/IOS_20XR_20Entitlement
					Wiki - Backplane EEPROM > http://viking-twiki1/twiki/bin/view/Viking/SoftwareEntitlement#Backplane_EEPROM
					Cisco Docs - Software License Operations White Paper : http://www.cisco.com/web/Cisco_IOS_XR_Software/pdf/ASR9000_SWE_User_whitepaper.pdf
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					q-license-dev@cisco.com
					""",

				'Multicast/mVPN':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show lpts pifib hardware police loc [] | in IGMP|PIM
					show controller np counters loc []              // ( ingress / egressLC)
					show controller fabric fia bridge stats         // ( Ingress LC)
					show controller fabric fia stats                // ( egress LC)

					RP Processes:
					show igmp traffic
					show igmp group summary
					show igmp interface
					show pim group-map
					show pim topology route-count
					show pim neighbor
					show mrib client
					show mrib route summary

					LC Processes:
					show mfib route
					show mfib connections
					show mfib nsf
					show mfib hardware route olist location []
					show mfib hardware connection location []
					show mfib hardware ltrace location []
					show mfib hardware interface location []
					show controller np counters all
					show controller np struct [id] all
					show controller np summary all

					show uidb data location [] bundle-ether [id] ingress
					show mfib ipv4 hardware interface detail location []
					show mrib route [ ] detail                                   // ( to compare MFIB and MRIB)
					show mfib route [ ] detail location [ ]
					show mfib ipv4 hardware interface detail location []
					show mfib hardware route statistics location []
					show mrib route
					show pim topology
					show mrib route
					show igmp groups
					show mfib interface                                          // ( enabled, mcast packets in/out)

					RPF Failures:   // ( Verify ingress or egress counts are incrementing and drops should not increment)
					clear mfib counter location []            // ( to clear mfib counters)

					show mfib ipv4 counter location []         // (   Verify ingress or egress counts are incrementing and drops should not increment)
					show mfib hardware route olist [ source/group address ] location []  // ( Output shows if mfib hardware has an appropriate set of output interfaces)
					show mfib ipv4 route statistics detail location []           // ( verify RPF FAILURES IN HW MFIB STATS
					show mfib ipv4 route  [] detail  location []                  // ( RPF faliures)
					show mfib ipv4 route [] detail location []                    // (Rate per route (Rate, ACC:Y))
					show mfib ipv4 route rate []                                        // ( verify route rate)
					show bgp ipv4 mdt vrf [vrf-name]                               // ( look for MDT group address)

					show bundle trace all location []
					show bundle trace process adj loc []
					show mfib trace location []
					show mfib hardware ltrace location []
					show mlib trace location []
					show mrib trace  location  []
					show mrib trace pim
					show pim trace mrib

					VRF:
					show pim vrf [vrf name] topology [MC group address] [source address]
					show mrib vrf [vrf name] route [MC group address]  detail
					show mfib vrf [vrf name] route  [MC group address] [source address] detail location []                      // ( On LC )
					show mfib vrf [vrf name]  hardware route sta det  [source address] [MC group address] location []
					show mfib vrf [vrf name]  hardware route ol  [source address] [MC group address] location []

					RPF:
					show pim vrf [vrf name] rpf
					show mfib hardware ltrace location [LC location]
					show mfib trace location [loc]
					show mlib trace location [loc]
					show mrib trace location [loc]
					show mrib route [S,G] detail
					show mfib route [S,G] detail
					show mfib route [S,G] detail location [ingress LC]
					show mfib hardware route olist detail [S,G] location [ingress LC]
					show mfib hardware route olist shadow [S,G] location [ingress LC]
					show mfib hardware route olist hex-dump [S,G] location [ingress LC]
					show mrib fgid info []
					admin show controllers fabric fgid information id []
					admin show controllers fabric fgid information id [] diagnostics
					show mfib route [S,G] detail location [egress LC]
					show mfib hardware route olist detail [S,G] location [egress LC]
					show mfib hardware route olist shadow [S,G] location [egress LC]
					show mfib hardware route olist hex-dump [S,G] location [egress LC]
					clear mfib database location []       // ( Clear mfib database to force re-syncing from mrib to mfib, and re-program LC HW mfib)
					show pim vrf all join-prune st        // (  verify MDT MTU)

					show tech multicast
					show tech multicast hardware
					show tech multicast vrf [vrf-name-1]                                      // ( if there are multiple VRFs involved in the failure, info must be collected on a per-VRF basis)                                                                                                                       default VRF and all affected customer-configured VRFs.

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Cisco Support Forum - Multicast troubleshooting Document > https://supportforums.cisco.com/sites/default/files/legacy/1/9/6/91691-asr9k-multicast-troubleshooting-external.pdf
					Ask ASR9K Knowledge Base - Troubleshooting Multicast FGID and MGID > http://asr9k.cisco.com/ask/index.php?action=artikel&cat=11&id=518&artlang=en
					TechZon - MGID and FGID for multicast traffic on ASR9k > https://techzone.cisco.com/t5/ASR-9000/MGID-and-FGID-for-multicast-traffic-on-ASR9k/ta-p/178440
					Ask ASR9K Knowledge Base - Architecture System Understanding Multicast performance on the ASR9000 > http://asr9k.cisco.com/ask/index.php?action=artikel&cat=15&id=161&artlang=en
					TechZone - MVPN Generic Encap forwarding packet loss troubleshooting > https://techzone.cisco.com/t5/ASR-9000/ASR9K-MVPN-Generic-Encap-forwarding-packet-loss-troubleshooting/ta-p/798736
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					""",

				'NetFlow':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show flow monitor [monitor name] cache brief location []
					show flow monitor [monitor name] cache match layer4 source-port-overloaded eq 179 location []        // (example to match BGP)
					show flow monitor [monitor name] cache sort counters bytes top brief location []                                       // ( for sorting)
					show flow exporter-map [exporter-map name]
					show flow exporter [exporter-map name] location []
					show flow monitor-map [monitor-map name]
					show flow monitor [monitor-map name] location []
					show sampler-map [sampler-map name]

					Matching BGP:
					show flow monitor [monitor-map name] cache match layer4 source-port-overloaded eq 179 location []

					Sorting:
					show flow monitor [monitor-map name] cache sort counters bytes top brief location []
					show flow exporter-map fem
					show flow exporter fem location []
					show flow monitor-map rtbh
					show flow monitor rtbh location []
					show sampler-map rtb

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - IOX Netflow > http://wiki-eng.cisco.com/engwiki/IOX_2dNetflow
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					q-netflow-dev@cisco.com
					""",

				'NP Network Processor':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show controllers np ports all location []                       // ( shows ports to NP mapping)
					show controllers np interrupts all all location []          // ( check for NP interrupts)
					show controllers np soft-errors all all location []          // ( look for SW detected NP errors)
					show controllers np descriptions location []                // ( Lists NP counters description)
					show tech np                                                                 // ( check media for NP related files, ( NPDatalog, NPdrvlog ) )

					NP Drops:
					show controllers np ports all location []                    // ( issue multiple times)
					clear controller np counters all                               // ( to clear counters if needed)
					show controllers np counters all location []

					QoShal:   // Verify traffic on TM
					show qoshal  punt-queue np []  location []                                           // ( NP to Linecard CPU)
					show qoshal default-queue interface [type] [interface number]
					show qoshal default-queue subslot [number] port [interface port number] location []
					show qoshal loopback-queue np [np number] location []                                              // (  internal loop processing, like DB flood)


					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					TechZone - NP Lockups, fast resets explained > https://techzone.cisco.com/t5/ASR-9000/ASR-9000-NP-Lockups-Summary/ta-p/631644
					Wiki - Dataplane & NP Lockup Triage Flowchart > https://wiki.cisco.com/pages/viewpage.action?pageId=4473421
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					""",

				'nV Cluster':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show nv edge control-link-port-counters [0-1]  [port Id]
					show nv edge control control-link-protocols location []
					show nv edge control-link-sfp [0-1]  (port Id)
					show nv edge control driver-process-data location []
					show nv edge control driver-trace all
					show nv edge data client [0-4294967295]  client jobid
					show nv edge data forwarding location []
					show nv edge data interfaces to-rack [0-1] [destination rack number]
					show nv edge data intfmon location []
					show nv edge data ports location []
					show nv edge data protocol [0-64]  [port number]
					show nv edge data tables rack [0-1] [Rack number]
					show nv edge data trace all
					admin show dsc stats
					admin show dsc trace [stats | location| ]

					show tech-support nv-edge [location []| rack []]

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - Loading Cluster Systems > http://viking-twiki1/twiki/bin/view/Viking/LoadingClusterSystem
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					""",

				'nV Satellite ASR9000v':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show nv satellite status
					show nv satellite status satellite [ 100-65534]                       // ( Satellite ID to filter by)
					show nv satellite protocol discovery brief                        // ( discovery protocol state on every ICL link)
					show nv satellite protocol discovery
					show nv satellite protocol discovery interface [ type] [ interface number]
					show nv satellite protocol control
					show interface [ type] [ interface number]                        // ( at both sides)
					show nv satellite hardware satellite [ sat number]
					show uidb data location [] [interface type] [ interface number]  ingress       // ( look for satellite flags are set, if bundle will on bundle not link)

					show nv satellite trace internal hardware all location [ICL_Linecard_Location]
					show tech-support satellite

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					TechZone - ASR9000 : Satellite Troubleshooting Guide > https://techzone.cisco.com/t5/ASR-9000/ASR9000-Satellite-Troubleshooting-Guide/ta-p/604936
					Cisco Support Forum - ASR9000 : Satellite Troubleshooting Guide > https://supportforums.cisco.com/t5/service-providers-documents/asr9000-satellite-troubleshooting-guide/ta-p/3143505
					Wiki - Viking Satellite TroubleShooting: http://ptlm-linux1/twiki/bin/view/Viking/VikingSatelliteTroubleShooting
					TechZone - ASR9k nv satellite console port commands > https://techzone.cisco.com/t5/ASR-9000/ASR9k-nv-satellite-console-port-commands/ta-p/478865
					Wiki - 9000v Satellite Client PI debug > http://ptlm-linux1/twiki/bin/view/Viking/ClientDebuggingReference
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					xr-nv-satellite-support@cisco.com
					asr9k-satellite-eng-support@cisco.com
					cs-satellite-support@cisco.com
					""",

				'Packet Path':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show  controllers [ type] [interface number] stats                    // ( PHY stats before NP , all stats commands issue multiple times)
					show controller np counters all location []                                   // ( NP stats for a given location )
					clear controller np counters all location []
					show controller fabric fia bridge stat location []
					show controller fabric fia stat location []
					show controller fabric crossbar statistics instance [ 0 | 1 ]  location []        // ( RSP fabric counters
					show controllers np portMap [ all | location [] ]                                               // ( to show port mapping on NP to Virtual Queues)
					show controllers np ports [ all | location [] ]                                                       // (  shows NP port mapping)

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Cisco Doc - ASR9k Packet flow commands > http://www-tac.cisco.com:81/~ampallam/ASR9k/asr9k-amar-troubleshooting.pdf
					Cisco Doc - Troubleshooting Traffic Forward Path > http://www-tac.cisco.com:81/~ampallam/Buddy%20Docs/A9K-Forwarding-TS-Zhongzhen.pdf
					Ask ASR9K Knowledge Base - Troubleshooting System Packet flow commands > http://asr9k.cisco.com/ask/index.php?action=artikel&cat=12&id=30&artlang=en
					Cisco Support Forum - Troubleshooting packet drops and understanding NP drop counters > https://supportforums.cisco.com/docs/DOC-15552
					Wiki - SPP Troubleshooting Debug > http://viking-twiki1/twiki/bin/view/Viking/SppDebug
					Wiki - Debugging Viking Fabric Issues > http://ptlm-linux1/twiki/bin/view/Viking/VikingDebuggingFabricIssues
					Debugging Input drops - Cisco Support Community
					TechZone - Capture Dropped packets on Typhoon NPs with "monitor np counter" command > https://techzone.cisco.com/t5/ASR-9000/Capture-Dropped-packets-on-A9SR9000-Typhoon-NPs-with-quot/ta-p/159696
					Wiki - Viking (Trident) Microcode Debug Trace > http://viking-twiki1/twiki/bin/view/Viking/DebugTrace
					Wiki - Viking Native Debugger > http://viking-twiki1/twiki/bin/view/Viking/NpDbgMain
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					""",

				'Power':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					admin show power history rack [ 0 | 1 ]                    // ( will normally be 0)
					admin show environment all
					admin show diag power-supply
					admin show diag power-supply eeprom-info.
					admin show diag chassis eeprom
					admin show inventory chassis

					show controllers power-monitor trace
					show inventory trace error
					show shelfmgr trace
					show controllers power-monitor trace
					show controllers i2c server trace
					admin show tech-support shelfmgr

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Ask ASR9K Knowledge Base - The event codes for admin show power history > http://asr9k.cisco.com/ask/index.php?action=artikel&cat=1&id=693&artlang=en
					https://techzone.cisco.com/t5/XRv-9000/bd-p/XRv_9000_Board
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					""",

				'PRM (Primitive Resource Manager)':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show prm stats summary [ location | np ]
					show prm server clinfo location []
					show controllers np interrupts all all location []                     // (  3 times with 5 sec interval)
					show controllers np soft-errors all all location []                     // (  3 times with 5 sec interval)
					show processes prm_server_tr location []                                // ( Note down the JID and PID of the process)
					show process threadname [JID] location []
					follow process [PID] iteration 10 stackonlyloc []
					show netio client location []
					show processes memory [JID] location []

					show prm server trace [ error , event, hal, internal, init, ] location []
					dumpcore running prm_server_ty loc []
					debug prm general internal location []


					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - ASR9K PRM > https://wiki.cisco.com/display/HEROBU/ASR9K%20PRM
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					""",

				'QOS':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show prm server tcam summary all qos [np[0,1,x] location []
					show qoshal resource summary np 1 location []                // ( allocated resources per NP)
					show controller np struct 2 [np[0,1,x] loc [lc]              // ( shows how many are used )
					show controllers np counters [np id] location []             // ( Issue 2-3 times with a few seconds gap)
					show controllers np tm counters [np id] location []                         // ( Issue 2-3 times with a few seconds gap)
					show qos-ea km policy [policy-map] vmr int [type] [int-num] [hw | sw]
					show policy-map interface [type] [ interface number] [ input | output ] location []    // ( On ingress and egress for traffic, issue multiple times)
					show qos interface [type] [ interface number] [ input | output ] location []           // ( On ingress and egress for traffic)
					show qos-ea interface [type] [ interface number] [ input | output ] location []        // ( This gives the token bucket address)
					show controllers np ports all location []                                              // ( Which NP maps to interface)
					show qoshal  punt-queue np []  location []
					show qoshal queue np [np] tm [0] level 0 qid 0 1 location []            // (  total buffers used by the NPU/Traffic manager
					show qoshal queue np [np] tm [tm] level 1 qid 0 1 location []
					show qoshal default-queue port [front-port] location []                 // ( find the NP/TM #)
					show qoshal default-queue port [] location []                           // ( Default queues the port # is the actual front port)
					show qoshal default-queue port 3 location []
					show qoshal loopback-queue np 0 location []

					show tech qos pd

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					TechZone - Introduction to ASR9K QoS Hardware Programming and Troubleshooting > https://techzone.cisco.com/t5/ASR-9000/Introduction-to-ASR9K-QoS-Hardware-Programming-and/ta-p/671597
					Ask ASR9K Knowledge Base - Understanding shaping, burst, token refresh(Tc), Bc, Be, PIR and CIR values > http://asr9k.cisco.com/ask/index.php?action=artikel&cat=18&id=451&artlang=en
					Cisco Jive - 9K QOS Policing: ASR9K QOS Policing : https://cisco.jiveon.com/docs/DOC-1807598
					Ask ASR9K Knowledge Base - Understanding show policy-map counters > http://asr9k.cisco.com/ask/index.php?action=artikel&cat=1&id=262&artlang=en
					Ask ASR9K Knowledge Base - What is counted in QOS policers and shapers > http://asr9k.cisco.com/ask/index.php?action=artikel&cat=18&id=75&artlang=en
					Topic - Ingress queuing is not supported on ASR9001: http://topic.cisco.com/news/cisco/mktg/ask-asr9k-tme/msg15428.html
					Topic - Ingress QoS on IronMan ASR 9001: http://topic.cisco.com/news/cisco/eng/cs-asr9k/msg52095.html
					Topic - ASR9K queue-limit: http://topic.cisco.com/news/cisco/cs/swisscom-nos-rs/msg00298.html
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					""",

				'Scale ACL':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show access-lists [ ipv4 | ipv6 ] [ acl name ]
					show access-lists [ ipv4 | ipv6 ] acl_hw_1 hardware [ egress | ingress ] location []
					show access-lists [ ipv4 | ipv6 ] list [1-2147483646]   // ( Sequence number to display

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Ask ASR9K Knowledge Base - Understanding access-list log messages > http://asr9k.cisco.com/ask/index.php?action=artikel&cat=1&id=450&artlang=en
					Wiki - asr9k scale acl > https://wiki.cisco.com/display/HEROBU/asr9k%20scale%20acl
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					xr-acl-scale-dev@cisco.com
					""",

				'Smart Licensing':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show run call-home
					show call-home detail
					show call-home profile all
					admin show license status
					admin show licence pool
					admin show license version
					admin show license register-status
					show call-home smart-licensing statistics
					admin show license all

					show call-home trace error
					show call-home trace all
					admin show license trace

					show tech-support call-home
					admin show tech-support license
					admin show tech-support smartlic

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Cisco Docs - Smart Licensing on the ASR9000 Platform > http://www.cisco.com/c/en/us/support/docs/routers/asr-9000-series-aggregation-services-routers/200011-Smart-Licensing-on-the-ASR9000-Platform.html
					TechZone - Smart Licensing on the ASR9000 Platform > https://techzone.cisco.com/t5/ASR-9000/Smart-Licensing-on-the-ASR9000-Platform/ta-p/775986
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					asr9k-smart-lic@cisco.com
					xr-sch@cisco.com
					""",

				'SPAN (Switched Port Analyzer)':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show monitor-session status detail
					show monitor-session counters
					show controllers np struct [37|15] detail all-entries interpret all location []                 // ( 37: formatted SFT (SPAN forwarding Table)
																													// (15: formatted SDT (SPAN Destination Table)
					show l2vpn xconnect
					show l2vpn xconnect type monitor-session-pw
					show l2vpn atom-db detail
					show l2vpn forwarding
					show l2vpn forwarding monitor-session location []
					show l2vpn forwarding monitor-session [span session name] location [..]
					show l2vpn forwarding hardware

					show monitor-session trace                    // ( SPAN PI)
					show monitor-session platform trace      // ( SPAN PD)
					show l2vpn trace                                     // ( L2VPN PI )
					show l2vpn platform trace                       // ( L2VPN PD )

					show tech-support span
					show tech-support l2vpn

					debug monitor-session                          // ( SPAN Platform Independent ( PI ))
					debug monitor-session platform             // ( SPAN Platform Dependent ( PD ) )
					debug l2vpn                                             // ( L2VPN PI)
					debug l2vpn forwarding
					debug l2vpn forwarding platform             // ( L2VPN PD )

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Cisco Support Forum - ASR9000/XR: How to use Port Spanning or Port Mirroring > https://supportforums.cisco.com/document/60596/asr9000xr-how-use-port-spanning-or-port-mirroring
					Wiki - SPAN Troubleshooting > http://enwiki.cisco.com/SPAN/Troubleshooting
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					iox-span-dev@cisco.com
					viking-span@cisco.com
					q-l2vpn-dev@cisco.com
					viking-l2-sw@cisco.com
					""",

				'uRPF (Unicast Reverse Path Forwarding)':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show cef ipv4 interface [type] [interface number]
					show cef ipv4 drops location []
					show cef ipv4 [ prefix ] hardware [ ingress | egress ] det location []
					clear cef ipv4 drops loc []
					show netio idb [type] [interface number
					show uidb data location [loc] [type] [interface number] ingress         // ( uRPF info, flags, mode)
					show controller np
					show cef platform trace rpf

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					TechZone - ASR9k Thor(SIP-700) : Thor IP URPF > https://techzone.cisco.com/t5/IOS-XR-PD-A9K-SIP-700-LC-Thor/ASR9k-Thor-SIP-700-Thor-IP-URPF/ta-p/988268
					TechZone - Main search and New Issues > https://techzone.cisco.com/t5/ASR-9000/bd-p/xr_asr9000
					cs-asr9k@cisco.com
					""",

				'VSM (Virtualized Services Module)':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show controllers switch data-path summary location []
					show virtual-service list
					show virtual-service detail name
					show virtual-service global
					show log | i service_msg

                    show tech-support vsm location [] file media:filename
                    show tech-support services cgn

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Cisco Support Forum - ASR9000/XR CGv6 on VSM: CGN / NAT44 Deployment Guide > https://supportforums.cisco.com/document/12019576/cgv6-vsm-cgn-nat44-deployment-guide
					TechZone - ASR9K CGv6 on VSM troubleshooting guide > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/ASR9K-CGv6-on-VSM-troubleshooting-guide/ta-p/569228
					TechZone - ASR9000 VSM Interface Mapping (NP, Marvell switch, SecGW VM, vIOS VM, CGN VM) > https://techzone.cisco.com/t5/ASR-9000/ASR9000-VSM-Interface-Mapping-NP-Marvell-switch-SecGW-VM-vIOS-VM/ta-p/608850
					Cisco Docs - Carrier Grade IPv6 over VSM > http://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/asr9k_r5-1/cg_nat/configuration/guide/cgnat_51/cgn_vsm.html
					Cisco Docs - ASR9K VSM(Forge) Service Blade PPT > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/VSM/Docs/ASR9K-VSM_for_TAC.pptx
					Cisco Docs - Trouble Shooting Guide for the Forge Line Card Doc > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/VSM/Docs/TSG_doc_for_the_VSM.docx
					""",
                 'Virtual 9K':"""
                    Useful Commands for Troubleshooting: //( Some commands syntax could vary according to platform or version)
                    Base: //( use 9K Base commands in addition to below , some may not apply to v9000 )
                    show platform
                    show logging
                    show version brief
                    show install active summary
                    show running
                    show license platform summary
                    show license all //( make sure authorized )

                    Packet Flow: //( [ NIC] [RX-> DPDK,loadbal optional ] [Worker-> EthernetClass, Ingress Fdw, Egress Fdw ] [TX-> Traffic MGR QoS, Interface Out, DPDK Dvr] [ NIC ]
                    //( XR Container - DPC SPP )

                    DPC: //( DPC ( Data Path Controller ) is part of XR Container will be in LC Container in later releases)
                    show controllers dpc interface trace all
                    show controllers dpc rm dpa // ( polling status with DPA , up , RRT if > 1 min = syslogs or LC relaod)
                    show controllers dpc rm resource thread // ( process running in control plane )
                    show controllers dpc rm resource thread [ thread Name ] details //( issue multiple times, pools Q stats crossing water marks )
                    show controllers dpc rm resource region //( should be showing GREEN , No out of resource state )
                    show controllers dpc rm resource table
                    show controllers dpc rm resource region
                    show controllers dpc rm trace event
                    show controllers dpc rm resource thread

                    //( UVF Universal Virtual Forwarding Container - DPA -> Packet Forwaring ( DPDK, VPP, and the XRv9000 dataplanecode )

                    DPA: //( DPA Data Path Agent Line Card )
                    show controllers dpa graph runtime //( realtime packet stats , vectors are packets thread has processed , vector/calls max 255 or drops)
                    show controllers dpa graph //( Packet Processing Graph )
                    show controllers dpa graph counters //( check for drops , issue multiple times )
                    show controllers dpa graph frame-queue // ( ( Inter-core frame queues can be displayed )
                    show controllers dpa log  // (displays log events for DPA agent - Line card, By default, only errors and several informational events are logged )
                    show controllers dpa threads
                    show ipv4 int brief
                    show controllers dpa port [ interface type ] [ number ] //( Can check for individual NIC , issue multiple times )
                    show controllers dpa interface [ type ] number ] //( will show drops and punts to control plane, issue multple times )
                    show controllers dpa statistics internal // ( For connectivity issue between DPC and DPA)
                    show controllers dpa statistics global // ( Traffic Punt, Inject, Drop counters Issue multiple times )
                    show controllers dpa statistics connection // ( For connectivity issue between DPC and DPA)
                    show controllers dpa buffers //( DPDK Packet Buffer
                    show controllers dpa efd //( Early Fast Discard if Configured )
                    show controller dpa fib [ipv4|ipv6] [<prefix>|summary]      // (displays FIB entries on the data plane)
                    show qos interface [ type ] [ number ] default-queues


                    SPP: //( Slow Path Punt/Inject packets travel from SPP <-> DPA - use tcpdump to dump the packets between DPA and SPP )
                    show spp node-counters //( SPP statistic , issue multiple times )

                    NETIO stats:
                    show netio forwarder statistics
                    show netio bypass
                    show netio client statistics

                    SYSTEM: //( admin VM )
                    admin show sdr
                    admin show virtual-platform                // (displays CPU & memory allocation to LXC)
                    admin show vm                                  // (we can check status of each LXC)
                    admin show sdr output
                    admin show sdr default-sdr reboot-history
                    admin show tech ctrace
                    admin show tech sdr_mgr
                    admin show tech HB-loss
                    admin show tech syslog

                    RUN: //( shell commands )
                    ifconfig
                    tcpdump -i eth-vf1.3074 // ( XR and UVF (LC) container -c is the count )
                    tcpdump -i eth-vf1.1794 // ( 3rd Party App )

                    Tech-Support:
                    show tech-support controllers dpc
                    show tech-support controllers dpa
                    show tech syslog  //( XR VM )
                    show tech processmgr

                    DEBUGS:
                    debug controllers dps packet-trace [ line , inject ] [ count 1-100 ]
                    show controllers dpa packet-trace //( from VPP graph )
                    clear controller dpa packet-trace //( clear before running again )

                    Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
                    Cisco Doc - IOS-XRv- VRR/ VPE Training links > https://cisco.jiveon.com/docs/DOC-1849133
                    vRR Training > https://docs.cisco.com/share/page/site/nextgen-edcs/document-details?nodeRef=workspace://SpacesStore/aafde301-6834-420c-83ca-f667d33b6148
                    Cisco Doc - Sunstone Troubleshooting Scenarios > https://cisco.jiveon.com/docs/DOC-112516
                    Wiki - Sunstone > https://wiki.cisco.com/display/SUNSTONE/Sunstone
                    Wiki - Sunstone Slow path debuging > https://wiki.cisco.com/display/SUNSTONE/Sunstone+Slowpath+Debugging
                    Wiki - Debug Arp > https://wiki.cisco.com/display/SUNSTONE/Debug+ARP
                    Sales - Virtual Routing IOS-XRv 9000 > https://salesconnect.cisco.com/#/program/PAGE-10324
                    TechZone- XRv9000 > https://techzone.cisco.com/t5/XRv-9000/tkb-p/XRv_9000_Board%40tkb
                    TechZone - Intro to V9K > https://techzone.cisco.com/t5/XRv-9000/Intro-to-XRv9k/ta-p/1003737
                    Cisco docs - Search links for XRv9000 > https://search.cisco.com/search?query=XRv%209000&locale=enUS
                    sunstone-dev@cisco.com , sunstone-pi@cisco.com, cs-xrv9k@cisco.com

               """ }




dict_CRS = {
                'ACL': """
                   	Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show  access-lists afi-all
					show  access-lists ipv4 summary
					show  access-lists maximum detail
					show  access-lists ipv4 [ ACL ] hardware [ingress | egress] [details | implicit | interface | loc | sequence ]
					show  access-lists usage pfilter location [ node-id | all ]
					show  access-lists hardware ingress drop-count interface [ type ] [ number ] locattion []
					show  access-lists hardware egress drop-count interface [ type ] [ number ] locattion []
					show  access-lists usage pfilter location []    //( Shows packet filter acl base usage per location or all )

					show  access-lists trace intermittent
					show  access-lists trace critical

					Relevant Traces:
					show  im trace
					show  pfilter-ea ipv4 trace [fast | slow] [all | errors | events]   //( Packet filter , define area of focus or all )
					show  pfilter-ea ipv6 trace [fast | slow] [all | errors | events]
					show  pfilter-ma trace

					Debugs:
					debug pfilter-ea all
					debug pfilter-ea errors
					debug pfilter-ea info
					debug pfilter-ea trace

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Techzone - CRS ACL SPAN support > https://techzone.cisco.com/t5/CRS-Carrier-Routing-System/CRS-ACL-SPAN-support/ta-p/742519
					crs-acl-support@cisco.com
                    """,

				'Base Commands':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show version
					show log
					show install log
					show redundancy
					show context
					show environment all
					show run
					show configuration commit list
					show proc blocked location all
					admin show configuration commit list
					admin show install active sum
					admin show platform
					admin show inventory chassis
					admin show inventory
					admin show diag
					admin show hw-module fpd location all
					admin show reboot history location []

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - IOS-XR > https://wiki.cisco.com/display/GSRTR/IOS-XR
					Techzone - XR OS and Platforms > https://techzone.cisco.com/t5/XR-OS-and-Platforms/ct-p/xr
					Jive - CRS Addition Links > https://cisco.jiveon.com/docs/DOC-245614
					XRGeeks > http://xrgeeks.cisco.com/
					XR PI/PD DE Alias > https://cisco.jiveon.com/docs/DOC-619180
					"""	,


				'Bundle LACP':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show bundle status
					show bundle brief                                                                       // ( shows configured states of LACP, BFD, links, bandwidth)
					show bundle protect
					show bundle protect bundle-[type] [bundle # ]                       // ( shows last protect date/time, per port and current states)
					show bundle load-balancing bundle-[type] [bundle # ] detail location []
					show bundle infrastructure in-progress                                        // ( infrastructure hidden in some older releases)
					show bundle infrastructure mac-allocation
					show int bundle-[type] [bundle # ]  detail
					show bundle bundle-[type] [bundle # ]
					bundle-hashow bundle-(bundle if#)                                             // ( this command is to help troubleshooting/evaluating flows over link bundle interfaces)

					show lacp                                                                    // (  View LACP states , Id for local ports)
					show lacp count                                                           // ( LACPDU's Port,  Sent, Received, Excess, Expired Defaulted , timeouts )
					show lacp bundle-[type] [bundle # ]                         // ( displays info about Link Aggregation Control Protocol (LACP) ports and their peers)
					show lacp system-id
					show lacp counters bundle-[type] [bundle # ]          // ( LACP Tx/Rx packets should match or increasing together, if no ,indication to LACP drops)


					Additional Relevant Checks:
					show uidb index bundle-[type] [bundle # ] location []
					show arp                                                                                                               // ( bundle-ether)
					show cef
					show cef ipv4 summary                                                                                  // ( displays (CEF) IPv4 hardware status and configuration information)
					show cef adj bundle-[ type] [bundle # ] hard ingress detail location []      // ( use location of the bundle members, use the bundle hashow command)
					show cef adj bundle-[type] [bundle # ]  hard egress detail location []       // ( use location of the bundle members, use the bundle hashow command)
					show cef hardware [ ingress | egress ] detail location []
					show adj detail hardware location []
					show adj remote detail hardwar location []

					Traces/Debugs and Show Techs:
					show bundle trace
					show bundle trace all location []
					show bundle trace process all location []
					show tech bundles file [media]:[filename]
					show tech bundles interface bundle-type [bundle #] file [media]:[filename]
					show tech pfi file [media]:[filename]
					debug lacp packet[Bundle-Ether| Bundle-POS| GigabitEthernet | POS | TenGigE]


					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - CRS -Bundles Self Serve wiki > https://wiki.cisco.com/display/GSRTR/CRS+-Bundles+Self+Serve+wiki
					Wiki - CRS Bundle Troubleshooting > http://wiki-eng.cisco.com/engwiki/CRS_25BundleInterfaces#head-9785378c2cc8368b286317b04e23c5709a05ada3
					Techzone - Troubleshooting CRS Bundles Forwarding  > https://techzone.cisco.com/t5/CRS-Carrier-Routing-System/Troubleshooting-CRS-Bundles-Forwarding/ta-p/827356
					Wiki - Bundle Infra Troubleshooting and Support > http://enwiki.cisco.com/BundleInterfaces/Support
					Wiki - Architecture & Tshoot presentation > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/q-tac/Troubleshooting/ChalkTalks_IOS_XR_Team/Bundle_on_IOS_XR/Bundle_on_IOS_XR.ppt
					""",

				'Capture dropped packet':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show captured packets ingress location [ node ]    //( option hexdump dump, last (  show the last [X] pkts in the queue ), single-line ( show all output for a packet )in a single lineThe buffer holds about 200 packet entries and rolls)
					clear captured packets ingress location [ node ]

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Cisco Suppport- Troubleshooting Commands > https://www.cisco.com/c/en/us/td/docs/routers/crs/software/crs_r4-0/adv_system/command/reference/b_ar_crs1/b_ar_crs1_chapter_01.html#wp2306296788

					""",

				'CGN':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show install active sum  | inc hfr-cgn-p.pie-      // ( pie must installed )
					show route vrf [ vrf name]   // ( Inside vrf)
					show route vrf [ vrf name ]  // ( Outside vrf)
					show int serviceapp 1 accouting    // ( In From CGN to Inside and Out From Inside to CGN )
					show int serviceapp 2 accouting    // ( In From CGN to Outside and Out From Ouside to CGN)

					show cgn demo inside-translation protocol tcp inside-vrf Inside inside-address  [ip] port start  1 end 65535
					show cgn demo outside-translation protocol tcp outside-vrf Outside outside-address  [ip] port start  1024 end 65535
					show cgn demo statistics
					show cgn demo statistics summary
					show cgn demo pool-utilization inside-vrf Inside address-range [start ip] [end ip]
					clear cgn nat64 stateful sf1
					clear cgn nat44 NAT-2 ipaddress [ip address]  // ( Internal IP)

					show tech-support services cgn
					show tech-support cgn

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - Carrier Grade NAT > https://wiki.cisco.com/display/GSRTR/Carrier+Grade+NAT
					ask-cgn-eng@cisco.com
					q-cgn@cisco.com
					cgn-dev-group@cisco.com
					""",
				'Control Ethernet':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					admin show controller fabric connectivity all details                                // ( On every RP/SC (active and standby) of each chassis, collect all of the following )
					admin show controller switch [0 and 1] [ ports and and stats ] location []
					admin show controller switch [ ports and stats ] location []
					admin show controller backplane ethernet detail location []
					admin show controller backplane ethernet clients all location []
					admin show controller backplane ethernet client [num] statistics location []      // (  repeat num for each of the client listed in prev cmd output)
					admin show controller backplane ethernet multicast group all location []
					admin show controller backplane ethernet trace location []
					admin show spantree mst 1 detail location []
					admin show controller switch udld location []
					admin show controller switch inter-rack port all location []
					admin show controller switch inter-rack udld all location []
					admin show controller switch inter-rack stp location []

					admin show controller back ethernet detail location [destination]     // ( all nodes should be visible)

					Check if Qnet is working:                                           // ( lwm_ping to a destination node)
					run
					lwm_ping                                 // (usage; lwm_ping [-v] -n [node_name] [-s size] [-i interval(ms)] [-c count])
					ls /net                                       // ( show node list  )

					lwm_ping -n  node0_2_CPU0 -c 10              // (  Connected via /net//node !!!!!!!!!!#)
					lwm_ping -n  node0_2_SP -c 10                  // (  to HBA on node node0_2_SP !!!!!!!!!!#)


					Check if Qnet packets are flowing:
					admin show controller back ethernet client 1 statistics loc [src-node]
					show controllers backplane ethernet clients 1 statistics location 0/rp1/cpu0
					ceping                                                   // ( unicast CE ping)
					mceping                                                  // ( muliticast CE ping, use mceping and gsp_ping and compare results to find out of the issue is proc related.)
					gsp_ping

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					CRS Control Ethernet Wiki > https://wiki.cisco.com/display/GSRTR/Control+Ethernet
					""",

				'Fabric':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					Generic:
   					admin show run | inc shutdown                                        // ( look for links that could be admin down)
    				show log | inc fabric
                    show controllers fabricq summary location []
					show controllers fabricq statistics location [ ]
					admin show controllers fabric health
					admin show controllers fabric statistics
					admin show controllers fabric connectivity all detail                 // ( Check if Fabric connectivity in FSDB shows a similar status)
					admin show controllers fabric fsdb-pla rack all
					admin show tech-support fabric fast-snapshot
					admin show tech-support fabric fast-traffic
					admin show controller fabric trace all location []                      // ( on Muti-chassis make sure this is ran on fabric shelf)

					Barrier:  // (used by IngressQ and FabricQ ASICs for sequencing and packet reassembly)
					show controller ingressq block brm location [ ]
					show controller fabricq barrier aggr location [ ]

					Plane:
					admin show controllers fabric plane [plane_id]  statistics detail                    // ( Cell errors)
					admin show controllers fabric plane all detail                                        // ( Check the board status and plane status (at least 2 planes UP/UP, odd & even numbered))
					admin show controllers fabric plane all statistics                                  // ( traffic degradation / drops, check for the plane statistics, issue multiple times )
					admin show controller fabric plane all brief

					ASICs: // ( checks ASIC status - fsdb view of the asic)
					admin show controllers fabric sfe ingressq all detail                             // ( All Fabric ASICs UP/UP from FSDB & driver point of view)
					admin show controllers fabric sfe [s1,s2,s3] all detail                             // ( collect all s1,s2,s3 commands)
					admin show controllers fabric sfe fabricq all detail
                    admin show controllers fabricq summary location []
					admin show asic-errors fabricq [0 | 1  ] summ loc []
					admin show asic-errors all summ location []
					admin show controllers ingressq summary location []
					admin show controllers fabricq summary | i Node-id
					admin show controllers fabric fsdb-pla rack [ rack # | all ]

					Fabric Links:
					admin show controllers fabric link port fabricqrx all state mismatch                        // ( All necessary fabric links are UP/UP)
					admin show controllers fabric link health
					admin show controllers fabric link port ingressqtx all | inc UP.*DOWN
					admin show controllers fabric link port [ s1rx, s1tx, s2rx,s2tx,s3rx,s3tx] all | inc UP.*DOWN    // ( collect all s1,s2,s3 commands)
					admin show controllers fabric link port fabricqrx all | inc UP.*DOWN
					admin show controllers fabric link port [ s1rx, s1tx, s2rx,s2tx,s3rx,s3tx] statistics                     // ( collect all s1,s2,s3 commands, multiple times)
					admin show controllers fabric link port fabricqrx statistics

					Bundles:
					admin show controllers fabric bundle all detail  | incl UP | ex "72  0  0"                                      // ( look for bad links)
					admin show controllers fabric bundle port all
					admin show controllers fabric bundle port all stat

					EIO Status:
					admin show controllers ingressq eio links all location [ ]

					Fabric Data Flow :   Ingressq ===]  S1 ===] S2 ===] S3 ===] Fabricqrx
					admin show controller fabric link port [ s1rx, s1tx, s2rx,s2tx,s3rx,s3tx] | ex 'UP/UP|Unused|N/A'                   // ( To show the S1,S2,S3 rx and tx links that are DOWN)
					admin show controller fabric link port fabricqrx | ex 'UP/UP|Unused|N/A'                                                       // ( To show the Fabricqrx links that are DOWN)
					admin show controller fabric bundle all detail | ex  'DOWN|72    72     0          0|72    60     0          0'             // ( Alternatively Use the Show Fabric Bundle)

					Laser Optical power:  between S1 [-] S2 and S2[-]S3 (only available on the Multi-Chassis)
					admin show controller fabric pod optics power location [S1 cards]                                                     // ( provide the S1tx to S2rx)
					admin show controller fabric pod optics power location [S2 cards]                                                     // ( provide the S2tx to S3rx)

					Other Errors:
					admin show asic-errors all detail location [S13 card/S2 card]
					admin show controllers fabric trace fsdb-server fsdb-all location [ all | location ]

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - Fabric Debug and Triage  > https://wiki.cisco.com/display/GSRTR/CRS+Fabric
					Techzone - CRS Fabric Architecture and Troubleshooting  >  https://techzone.cisco.com/t5/CRS-Carrier-Routing-System/CRS-Fabric-Architecture-and-Troubleshooting/ta-p/630868
					q-fabric-dev@cisco.com
					cs-crs@cisco.com
					""",

				'Fabric BP Back Pressure':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show policy-map interface [] input
					show policy-map int bundle-ether [id] output
					show policy-map int bundle-ether [id] output | in "Class |rop"

					show controller ingressq stat loc []                                                                                    // (check stats discard drops and tail drops)
					admin show controller ingressq backpressure bpmem instance 0 location []             // ( On any card (as all LC will receive BP))

					admin show controller fabricq summary loc []                                                    // (to obtain the Fabric Destination Address)
					admin show controller ingressq block dcm taildrops [Q no.] [no. of Qs] [ASIC instance]  loc []        // (  to look for taildrops in these HP and LP queue for 4 specific queues)
					show controller fabricq queues loc []
					show controller fabricq queues id []instance [] location []                                       // ( only if needed by BU)
					show controller fabricq stat loc []                                                     // (  collect many times and monitor the BP asserted count)

					show controller egressq stat detail location []


					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Jive - CRS Fabric BP (Back pressure) TS doc >  https://cisco.jiveon.com/docs/DOC-1842353
					""",

				'CRSX Fabric':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version) // See CRS Frabic for other related commands

					Ingressqtx to s1rx:
					admin show controllers fabric link port ingressqtx all | i X/0/CPU0/ | i X/SM0/SP/               // ( Shows the ingressq inbar to fabricQ states)
					admin show controllers fabric link port ingressqtx all | i X/RP0/CPU0/ |i X/SM0/SP/           // ( show links from RP to fabric )

					S3tx to Fabriicqrx:
					admin show controllers fabric link port fabricqrx all | i X/0/CPU0/ | i X/SM0/SP/
					admin show controllers fabric link port fabricqrx all | i X/RP0/CPU0/ | i X/SM0/SP/

					POD OIM on FCC Chassis:
					show controllers fabric link port s2tx optics | F0/SM0/SP

					Load Balancing:
					admin show controllers sfe block os lut instance [] location                                    // ( Links are in pairs)
					admin show controllers sfe link-info rx 0 128 topo instance location                         // ( D flag indicate a forced Down link)
					admin show controllers sfe link-info tx 0 128 instance location

					Link Isolation:
					admin show controllers fabric bundle all detail | ex "DOWN" | ex "0 0"                        // ( links down)
					admin show controllers sfe link-info rx 0 108 topo instance range 0 2                     // ( links down from load balancing )
					admin show controllers fabric pod optics power location X/SM1/SP
					show controllers fabric pod optics power location []

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Techzone - CRS-X Fabric Tech Talk Session recording > https://techzone.cisco.com/t5/CRS-Carrier-Routing-System/CRS-X-Fabric-Tech-Talk-Session/ta-p/1108933
					Jive - CRS-X-Topaz-Deepdive pres > https://cisco.jiveon.com/docs/DOC-1050642
					cs-crs@cisco.com
					""",

				'CRS Fan':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show inventory trace fan
					admin show environment fans
					admin show environment trace
					admin show inventory fans
					admin show inventory loc [fc0 loc]
					admin show inventory loc [fc1 loc]
					admin show diag fans eeprom-info

					admin show cctl trace init loc [FC0 location]
					admin show cctl trace init loc [FC1 location]
					admin show cctl trace fan loc [FC0 location]
					admin show cctl trace fan loc [FC1 location]

					admin show i2c-ctrl trace error location all
					admin show i2c-ctrl trace error location [FC0 location]
					admin show i2c-ctrl trace error location [FC1 location]
					admin show i2c-ctrl trace common location all
					admin show i2c-ctrl trace common location [FC0 location]
					admin show i2c-ctrl trace common location [FC1 location]


					Shell Commands:
					run attach [FC0 or/and FC1 loc ]                                                    // ( Collect for fc1 / 0 and replace vefan instead of fc-fan/lc-fan if its a VE chassis)
					env show cardtype
					env show fc-fan host speed                                    // ( Card type LC-FAN)
					env show lc-fan host speed
					env show lc-fan host speed temp
					env show lc-fan host temp led
					env show vefan volt all
					env show vefan speed all
					env show vefan ver all
					env show vefan i2c-reset all
					run on -f node0_FC0_SP env show vefan speed all
					run on -f node0_FC1_SP env show vefan speed all
					admin show tech cctl

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					XR Geeks - CRS fan speed > http://xrgeeks.cisco.com/?q=content/crs-fan-speed
					XR Geeks - Troubleshooting CRS 1 / CRS 3 Fan Issues > http://xrgeeks.cisco.com/?q=content/troubleshooting-crs-1-crs-3-fan-issues
					XR Geeks - CRS Troubleshooting fan tray issues > http://xrgeeks.cisco.com/?q=content/crs-troubleshooting-fan-tray-issues
					Techzone - CRS 5.3.3 Fan Tray Major Alarm issue  > https://techzone.cisco.com/t5/CRS-Carrier-Routing-System/CRS-5-3-3-Fan-Tray-Major-Alarm-issue/ta-p/977649
					""",

				'GRE Tunnel':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show int tunnel-ip[id]
					show int tunnel-ip[id] ac location []

					show tunnel ip ma database [tunnel-ip[id]]                          // (To check tunnel MA TID DB)
					show tunnel ip ma database source                                    // (tunnel source is an interface so it has an entry in SRC DB)
					show tunnel ip ma database destination                        // (To check DST DB)
					show tunnel ip ma database ifh x                                 // ( ifhandle to find the tunnel id)
					show tunnel ip ea database location []                         // (check EA IDB
					show tunnel ip ea qt location []                                     // (Checking GRE tunnel qualification table (QT))
					show tunnel ip platform tunnel-ip [id] location []

					show uidb data tunnel-ip [id location []                     // (uIDB information resources associated with a given GRE tunnel)
					show uidb index location []

					show cef [prefix] hardware [ingress | egress] location []                            // (show the PLU memory)
					show cef adj tunnel-ip [] hardware [ingress | egress] location []                   // (Show TLU memory)

					show tech-support tunnel-ip
					show tunnel ip trace [platform ,ea ,ma ]

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - GRE > https://wiki.cisco.com/display/GSRTR/GRE
					Wiki - IOX GRE CHEAT SHEET > http://wiki-eng.cisco.com/engwiki/IOX_2dGRE_2dCHEATSHEET
					""",

				'Filesystem':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					admin show media location []
					admin fsck [media]:location []                       // ( check file system on disk FATs, Chains, Dir, lost files)

					admin show media location all
					admin show media location []
					show mirror
					show mirror loc all
					show mirror statistics
					show filesystem
					show redunduncy
					show file [media]:
					show file [media]: stats
					admin show active-fcd location all

					fsck [media]:

					show mirror trace
					show rdsfs trace error
					show rdsfs trace internal
					show rdsfs trace iofunc

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - CRS File System > https://wiki.cisco.com/display/GSRTR/CRS+File+System
					Doc - understanding and debugging FS issues > http://wwwin-eng.cisco.com/Eng/OIBU/Q/SW_Reviews/filesystem_faq.txt@5
					Wiki - Filesystem Troubleshooting Guide > http://wiki-eng.cisco.com/engwiki/Filesystem_20Troubleshooting_20Guide
					Wiki - Working with Filesystems > http://wwwin-stg-east.cisco.com/stg-tools/qnx/product/neutrino/user_guide/fsystems.html
					""",

				'Line card Shelf Manager Heartbeat':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					admin show platform | i [node]
					admin show shelfmgr node-history location []
					admin show shelfmgr notif location []
					admin show shelfmgr gsp-notif location []
					admin show shelfmgr power location []
					admin show shelfmgr database ccb location []
					admin show shelfmgr database fsmcb location[]
					admin show shelfmgr database ncb location []
					admin show shelfmgr databas plimcb location []
					admin show shelfmgr hardware
					admin show shelfmgr dcdc location []
					admin show shelfmgr hb-history location []
					admin show shelfmgr summary loc []
					admin show shelfmgr hardware

					admin show shelfmgr trace all location all
					admin show shelfmgr hb-history location  []

					dir [media]: location all
					dir [media]:/shutdown location all
					dir [media]:/ASIC-ERROR/ location all
					dir [media]:/asic_snapshots/ location all


					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Techzone -  Understanding and Troubleshooting Shelf Manager > https://techzone.cisco.com/t5/CRS-Carrier-Routing-System/Understanding-and-Troubleshooting-Shelf-Manager/ta-p/194274

					""",

				'NetFlow':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show flow platform pse policer-rate location []                                         // ( verify that the netflow policer-rate is correctly programmed in hardware)
					show controllers pse statistics location []                                                 // ( verify if there is any Netflow record drops by the PSE - issue multiple times)
					show flow platform producer statistics location []                                     // ( verify the amount of Netflow records received by Netflow producer - issue more than once)
					show uidb data [interface type] [interface number] location []                        // ( verify the Netflow configuration in UIDB)
					show cef vrf red ipv6 [ ipv6 address] hardware ingress detail location []         // ( verify the IPv6 Next Hop)
					show flow platform producer nh all location []                                                    // ( verify the address that the index maps to the correct address)
					show flow platform dba interface [interface type] [interface number]               // ( Verify that the interface is programmed against a region)
					show flow platform dba region all interfaces                                                         // ( Verify that the region is programmed correctly)
					show controllers pse statistics [ ingress, egress] location []                                // ( look for no netflow counters incrementing - issue multiple times)
					show controllers pse tcam region-list ingress netflow information entry hw loc []
					show flow exporter fe location []
					show flow monitor fmm cache location []
					show flow exporter-map fe
					show flow platform producer statistics loc []                                                      // ( issue multiple times)

					debug flow ea location []                                                             // ( If the configuration is failing, enable the ea debug )

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - CRS Netflow > https://wiki.cisco.com/display/GSRTR/CRS+Netflow
					Cisco Support - CRS Configuration Guide > http://www.cisco.com/c/en/us/td/docs/routers/crs/software/crs_r4-3/system_management/configuration/guide/b_sysman_cg43crs/b_sysman_cg43crs_chapter_0100.html
					""",

				'Packet Path':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)

					show platform drops detail location [loc]
					show controllers plim asic statistics interface [interface type] [ interface number ]        // ( ingress then egress side of the path)
					show controllers plim asic statistics summary location []                                     // ( ingress then egress side of the path issue multiple times)
					show controllers pse summary location []                                                      // ( ingress then egress side of the path )
					show controllers pse statistics ingress location []                                            // ( ingress then egress side of the path issue multiple times)
					show controllers cpuctfl ports ingressq pdma queue all active loaction []                        // ( ingressq then egressq side of the path )
					show controllers ingressq statistics location []                                              // ( ingressq then egressq side of the path issue multiple times)
					show controllers fabricq statistics loc []
					show controllers egressq queue all location [] | i Ins               // (  packets from PS, issue multiple times, look for traffic movement or stuck queues )
					admin show controllers fabric plane all
					admin show controllers fabric plane all statistics                      // ( verify how many cells have been transmitted across each plane details. issue multiple times)
					admin show controllers fabric connectivity all detail                   // ( check fabric card to line card connectivity details)
					admin show controllers fabric link port [port id] all statistics summary         // ( Check if any stage (S1, S2, S3) detected errors See CRS Fabric commands)

					show tech pfi all

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Techzone - PSE Counters glossary > https://techzone.cisco.com/t5/CRS-Carrier-Routing-System/CRS-PSE-Counters-Glossary/ta-p/808508
					Techzone -  CRS-3 Debug TCAM and CRS Packet Tracing > https://techzone.cisco.com/t5/CRS-Carrier-Routing-System/CRS-3-Debug-TCAM-and-CRS-Packet-Tracing/ta-p/49062
					Doc - Troubleshooting Path presentation > http://ecm-link.cisco.com/ecm/view/objectId/090dcae18442b8b9/versionLabel/CURRENT/versionLabel/CURRENT
					Wiki - Life of a Packet in CRS-1 > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/q-tac/Troubleshooting/LifeOfPacket/lifeofpacket.html
					Techzone - CRS Troubleshooting traffic black-hole scenarios > https://techzone.cisco.com/t5/CRS-Carrier-Routing-System/CRS-Troubleshooting-traffic-black-hole-scenarios/ta-p/614002
					Techzone - CRS-X packet walk through and commands > https://techzone.cisco.com/t5/CRS-Carrier-Routing-System/CRS-X-Overview-with-Packet-Walkthrough-amp-commands/ta-p/832250
					cs-crs@cisco.com
					""",

				'Environmental':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					admin show inventory
					admin show inventory trace power
					admin show inventory trace fan
					admin show inventory trace err
					admin show inventory trace build

					admin show environment all
					admin show environment power-supply internal
					admin show environment trace
					admin show diag power-supply
					admin show diag fans
					admin show diag details

					admin show i2c-ctrl trace common
					admin show i2c-ctrl trace error
					admin show cctl trace fan loc [] loc []
					admin show cctl trace api loc [] loc []

					admin show power allotted location [ ]
					admin show power capacity rack
					admin show power capacity summary
					admin show power summary rack
					admin show hw-module fpd location all
					admin show tech-support cctl


					""",

				'QoS':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show run policy-map                                                                                     // ( for all policy-maps involved in path)
					show run class-map                                                                                      // ( for all class-maps involved in path)
					show run interface [interface type] [ interface number]                            // ( for all interfaces involved in path)
					show qos interface [interface type] [ interface number]                           // ( shows hardware and its programming for the policy applied in rounded parameters)
					show fmgr interface [interface type] [ interface number] feature qos-all location []         // ( TCAM lookup entries and results for the policy)
					show fmgr interface feature qos-all hw location []
					show policy-map interface [interface type] [ interface number] [ input | output ]                 // ( QoS Statsistics , issue multiple times , look for drops)
					show interface [interface type] [ interface number]
					show interface [interface type] [ interface number] accounting
					show controllers pse statistics location []
					show controller pse statistic [ ingress | egress ] location []
					show uidb data
					show qos ea trace all location []
					show fmgr trace all location []
					debug qos control hardware [options] location []                                          // ( how the QoS policy is being processed in QoS EA)

					pwhe qos:  // (collect the output of following commands along with the commands above)
					show l2vpn pwhe detail interface [interface type] [ interface number]
					show l2vpn ma pwhe interface [interface type] [ interface number] private
					show im database interface verbose
					show controllers egressq queue from-interface [] location []
					show controllers egressq interface all location []
					show qos rm redq [queue-number] [ input | output ] hw loc []                                // ( redq Q# from show qos interface, ingress egress Q ID , read from hardware)
					show qos rm redq [queue-number]  [ input | output ] sw loc []
					show controllers egressq queue [queue-number ] hw loc []
					show controllers egressq queue [queue-number] sw loc []

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - IOX QoS  > https://wiki.cisco.com/display/GSRTR/CRS+QoS
					Wiki - IOX Qos  ( older ) > http://wiki-eng.cisco.com/engwiki/IOX_20QoS
					Techzone - How to find EgressQ Instantaneous Queue Depth for an Attached Service-Policy > https://techzone.cisco.com/t5/CRS-Carrier-Routing-System/CRS-How-to-find-EgressQ-Instantaneous-Queue-Depth-for-an/ta-p/844030
					Techzone - How to identify backpressure > https://techzone.cisco.com/t5/CRS-Carrier-Routing-System/How-to-identify-fabric-backpressure/ta-p/839040
					Techzone -  QoS Drops causing IPSEC tunnel connectivity Issues  > https://techzone.cisco.com/t5/CRS-Carrier-Routing-System/QoS-Drops-causing-IPSEC-tunnel-connectivity-Issues/ta-p/691867
					Wiki - Introduction to QOS on CRS-1 > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/q-tac/presentations/crs_qos/
					crs-qos-support@cisco.com (Triage/Bugs/Issues)
					crs-qos-dev@cisco.com (internal discussions specific to CRS-1)
					""",

				'SPA':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show hw-module subslot [] brief pluggable-optics
					show hw-module subslot [] status
					show controllers SONET []
					show controllers POS []
					show interfaces POS []
					show tech-support pos show run
					show spa-oc3-oc12 trace soNET [sonet interface]
					show spa-oc48 trace soNET [sonet interface]
					show controllers POS [POS interface] framer
					show controllers soNET [sonet interrface] framers

					show hw-module trace all level detailed location []
					show hw-module trace infra level detailed location []
					show hw-module subslot [subslot location ] ltrace spa location []
					show hw-module subslot [subslot location ] registers fpga
					show tech spa

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - CRS SPA/PLIM Platform > http://wiki-eng.cisco.com/engwiki/CRS_20SPA_2fPLIM_20Platform
					Wiki - CRS SPA Infra scenarios > https://wiki.cisco.com/display/GSRTR/CRS+SPA+Infra
					cs-crs@cisco.com
					""",
                'SRP' : """
                	Useful Commands for Troubleshooting:
					show srp topology    // ( will show nodes on ring, Last received packet should not be over configured value ( 5 sec ))
					show srp topology location []
					show srp topology interface srp [ R/S/I/P ]
					show controllers srp [ R/S/I/P ]     // ( check the physical setup Tx to Rx )
					show srp platform int srp [ R/S/I/P ]
					show srp ips int srp [ R/S/I/P ]   //( Must be in a "not wrapped" state, if wrapped indicates one side is down )
					show int srp [ R/S/I/P ] brief // ( Pass-through mode is when both sides of the interface cannot pass traffic,
					show srp failures interface srp [ R/S/I/P ]
					show arp //( Verify correct ARP table, show srp type and side connected )
					show dpt client location []
					show srp platform location []
					show srp failures location []
					show dpt interface location []
					show srp counters source location []
					show srp counters source interface  srp [ R/S/I/P ]
					show srp counters interface srp [ R/S/I/P ]
					show srp counters location []
					show srp interface []
					show srp ips location []
					show srp ips interface []
					show srp location []
					show srp srr interface []
					show srp srr location []
					show srp topology interface []
					show srp topology location []
					show srp transit location []
					show log | inc srp

					Debugs:
					debug srp ips
					debug srp topology

					Reference Links:
					Cisco Support - SRP Hardware Troubleshooting Guide > https://www.cisco.com/c/en/us/support/docs/optical/spatial-reuse-protocol-dynamic-packet-transport-srp-dpt/16182-srp-troubleshooting.html
					Techzone -  Spatial Reuse Protocol ( SRP) presentation> https://techzone.cisco.com/t5/CRS-Carrier-Routing-System/Spatial-Reuse-Protocol-SRP/ta-p/965962
					Doc - SRP Commands on Cisco IOS XR Software > https://www.cisco.com/c/en/us/td/docs/ios_xr_sw/iosxr_r3-2/interfaces/command/reference/int_r32/hr32srp.pdf
					Cisco Support - Understanding SRP Ring Topology > https://www.cisco.com/c/en/us/support/docs/optical/spatial-reuse-protocol-dynamic-packet-transport-srp-dpt/29860-understand-srp-topo.html
					q-srp-dev@cisco.com cs-crs@cisco.com
                    """
             }

dict_GSR12000 = {
                'Base Commands':"""
					Useful Commands For Troubleshooting:  //( Some commands syntax could vary according to platform or version)
					show version
					show log
					show install log
					show aps
					show redundancy
					show context
					show environment all
					show run
					show configuration commit list
					show proc blocked location all
					admin show configuration commit list
					admin show install active sum
					admin show platform
					admin show inventory chassis
					admin show inventory
					admin show diag
					admin show hw-module fpd location all
					admin show reboot history location []
					admin show sysldr trace all location[]    // )to see trace for specific LC)

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - GSR Top Troubleshooting Scenarios > https://wiki.cisco.com/display/GSRTR/GSR%20Top%20Troubleshooting%20Scenarios
					Wiki - IOS-XR > https://wiki.cisco.com/display/GSRTR/IOS-XR
					Techzone - GSR > https://techzone.cisco.com/t5/XR-OS-and-Platforms/ct-p/xr
					Jive - XR12k  Additional Links > https://cisco.jiveon.com/docs/DOC-245618
					XR Geeks > http://xrgeeks.cisco.com/
					XR PI/PD DE Alias > https://cisco.jiveon.com/docs/DOC-619180

					""",

				'Fabric':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					admin show controllers fabric  							//(3-4 times 30 sec interval)
					admin show controllers fabric fab-control
					admin show controllers fabric clock    					//(3-4 times 30 sec interval)
					admin show controllers fabric errors 					//( 3-4 times )
					admin show controllers fabric counters 					//(3-4 times)
					show controllers fia location [RP and LC #]  			//(from active-RP and the target LC , issue 2-3 times)
					show controllers fia register location [location]
					admin show controllers fabric fab-clk  					 //(3-4 times 30 sec interval)
					admin show controllers fabric xbar                      //(3-4 times 30 sec interval)
					admin show controllers fabric sca
					admin show controllers fabric csc-fpga
					show controllers fwd stat loc [ node ]

					admin show controllers fabricq drop detail
					admin show controllers fabricq errors detail
					admin show controllers fabricq frfab detail
					admin show controllers fabricq output detail
					admin show controllers fabricq queue detail
					admin show controllers fabricq registers detail
					admin show controllers fabricq tofab detail

					show techs:
					admin show tech shelf-management  file [media/path]    // large output

					Traces:
					admin show controllers fabric trace
					admin show fiad trace verbose location [location of RP/LC]or [no location = all]

					MBUS:
					admin show mbus can-error location  all               //(3-4 times 30 sec interval)
					admin show mbus counters location all                 //(3-4 times 30 sec interval)

					Environment:
					admin show environment voltage                         //(3-4 times 30 sec interval)


					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - Fabric Driver > https://wiki.cisco.com/display/GSRIN/Fabric+Driver
                    Wiki - IOS-XR C12K System Infrastructure > http://wiki-eng.cisco.com/engwiki/IOS_2dXR_20C12K_20System_20Infrastructure#head-0b05f6202aa759643440b69b8cb18f8075346713
					cs-xr12000@cisco.com

					""",

				'Line Card Failures':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show diag [] details
					admin show controllers fwd stats location [ node ]
					admin show hw-module fpd location all
					show  processes cpu location []
					show reboot history location []
					show  environment []
					show controllers plim asic spa bay [bay number ] location []
					show controllers pse ingreess statistics location []
					show  controllers pse egreess statistics location []
					show controllers plim spabrg-trace file [media]:[file name]
					show sysmgr trace
					admin show fpd trace location all
					admin show sysldr trace boot location []
					admin show fiad trace
					admin show fpd trace
					admin show tech shelf file [media]:[file name]
					show  tech pfi file [media]:[file name]
					show tech sysmgr file [media]:[file name]
					show tech cfgmgr file [media]:[file name]
					show tech sysdb file [media]:[file name]
					admin show tech gsp file [media]:[file name]
					show im statistics client location []

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - GSR IOX DEV > https://wiki.cisco.com/display/GSRIN/GSR+IOX+DEV
					Wiki - C12000 System Infra > https://wiki.cisco.com/display/GSRTR/C12000+System+Infra
					Wiki - SPA-Port Adapter Troubleshooting IOSXR > http://wiki-eng.cisco.com/engwiki/SPA_2dPort_20Adapter
					Wiki - E3 Hardware Debug Commands > http://wiki-eng.cisco.com/engwiki/E3_20Hardware_20Debug_20Commands
					Techzone - E3 Tetra IOS-XR Arch and Tshoot > https://techzone.cisco.com/t5/XR-GSR12000/E3-Tetra-IOX/ta-p/764441
					Techzone - E5 SPA IOS-XR Arch and Tshoot (Bluenose and Shashimi) > https://techzone.cisco.com/t5/XR-GSR12000/E5-SPA-IOX/ta-p/764442
					Text File - E3 Debugging > http://wwwin-eng.cisco.com/Eng/OIBU/WWW/q-tac/Troubleshooting/GSR_IOX/Troubleshooting/Debugging_E3_Linecard.txt
					Techzone - HFA (Alpha in E3 and Wahoo in E5) > https://techzone.cisco.com/t5/XR-GSR12000/C12000-HFA-Alpha-Wahoo/ta-p/764864
					Techzone - Linecard not booting up TS > https://techzone.cisco.com/t5/XR-GSR12000/LINE-CARD-Not-Booting/ta-p/768160
					cs-xr12000@cisco.com
					""",

				'RP Failures':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					RP Failures:
					show redundancy
					show reboot history
					show controllers fia location [node]     // (fabric errors, drops, clock)
					admin show controllers fabricq drop detail
					admin show controllers fabricq errors detail
					admin show controllers fabricq frfab detail
					admin show controllers fabricq output detail
					admin show controllers fabricq queue detail
					admin show controllers fabricq registers detail
					admin show controllers fabricq tofab detail
					admin show controllers fabric clock
					admin show controllers fabric csc-fpga
					admin show controllers fabric fab-clk
					admin show controllers fabric fab-control
					admin show controllers fabric sca
					admin show mbus can-error location [location ]
					admin show mbus counter location [location ]

					Traces:
					admin show sysldr trace boot location all
					show redundancy trace
					admin show fiad trace
					show sysmgr trace
					admin show mbus obfl trace

					Show Tech-Supports:
					admin show tech shelf file [media]:files_name ]
					show tech parser file [media]:files_name ]
					show tech pfi file [media]:files_name ]
					show tech sysmgr file [media]:files_name ]
					show tech cfgmgr file [media]:files_name ]
					show tech sysdb file [media]:files_name ]
					admin show tech gsp file [media]:files_name ]

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Cisco Support -  IOS XR Troubleshooting guide > https://www.cisco.com/c/en/us/td/docs/routers/xr12000/software/xr12k_r3-9/troubleshooting/guide/tr39xr12kbook/tr39boo.html#wp1067393
					Wiki - C12000 System Infra > https://wiki.cisco.com/display/GSRTR/C12000+System+Infra
					cs-xr12000@cisco.com
					""",

				'Node Isolation':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					admin show redundancy
					show reboot history location [loc]  // for both RPs
					admin show environment all
					show power-mgr detail
					show packet-memory summary
					admin show controllers fabricq drop
					admin show controllers fabricq errors
					show controllers fia location [ node ]    // (collect on all slots and issue 3 times per slot)
					admin show mbus can-error location all    // (collect 3 times)
					admin show mbus counters location all     // (collect 3 times)

					Traces:
					admin show redundancy trace
					admin show controllers fabric trace
					admin show sysldr trace all
					admin show sysdb trace
					show sysmgr trace
					show fiad trace

					Show tech-supports:
					admin show tech-support sysdb
					admin show tech-support sysmgr
					admin show tech-support gsp

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
                    Techzone - Troubleshooting document for GSR unreachable - Fault tree flowchat > https://techzone.cisco.com/t5/XR-GSR12000/Troubleshooting-document-for-GSR-unreachable-Fault-tree-flowchat/ta-p/560050?attachment-id=36388
                    cs-xr12000@cisco.com
					""",

				'mVPN':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show pim interface
					show pim vrf [VRF Name] interface
					show pim neighbor
					Show pim vrf [VRF Name] neighbor
					show pim vrf all mdt interface
					show pim rpf
					show pim group-map
					show mfib route rate
					Show pim vrf [VRF Name] group-map
					Show mfib vrf [VRF Name] route counter
					show mrib vrf [VRF Name] route
					show mfib vrf [VRF Name] route statistics

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Jive - IOX Multicast > https://cisco.jiveon.com/docs/DOC-1808564
					Techzone - mVPN Rosen Draft Cheat Sheet > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/mVPN-Rosen-Draft-Cheat-Sheet/ta-p/99352
					Techzone - Configure mVPN Profiles within Cisco IOS-XR > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Configure-mVPN-Profiles-Within-Cisco-IOS-XR/ta-p/600292
					Techzone - mVPN Master Page > https://techzone.cisco.com/t5/MPLS/mVPN-Master-Page/ta-p/630356
					PI related issue: q-multicast-dev@cisco.com
					XR12K: x-multicast-triage@cisco.com
					iox-igmp-snoop-dev@cisco.com
					""",

				'Bundle LACP':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show bundle
					show bundle [bundle-type] [ bundle number ]
					show bundle status
					show bundle load-balancing detail location [location]
					show lacp
					show lacp system-id
					show lacp counters [bundle-type] [ bundle number ]
					show interface [bundle-type] [ bundle number ] detail
					show iir interfaces name bundle-[type] [ bundle number ]
					show iccp counters

					Useful show tech-supports and traces:
					show bundle trace all
					show iccp trace
					show bundle trace process all
					admin show tech-support bundle file [ media]:[file_name ]

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Techzone - PI IOS XR Bundles > https://techzone.cisco.com/t5/XR-Platform-Independent-Topics/Troubleshooting-Guide-PI-IOS-XR-Bundles/ta-p/162412
					Wiki - C12000 Link Bundling > https://wiki.cisco.com/display/GSRTR/C12000+Link+Bundling
					Wiki - C12000 BFD Over Bundles > https://wiki.cisco.com/display/GSRTR/C12000+BFD+Over+Bundles
					cs-xr12000
					""",
				'Software Forwarding':"""
   					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					// troubleshooting ICMP/ping drops for icmp echo originated from other device on both sides
					Collect the below commands before and after sending the ICMP echo towards bearer CE:     // (execute 3 times at 30 second interval)
					show raw statistics pcb all location [location of active] RP
					show ipv4 traffic
					show netio clients location [ node ]
					show lpts pifib hardware police location [ node ]
					show controllers [ type] [ interface number ] stats
					show controllers pse statistics location [ node ]
					show interfaces [ type] [ interface number ] accounting
					show policy-map interface bundle-[type] [bundle number ] input
					show policy-map interface bundle-[type] [bundle number ] output

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki -  Help to troubleshoot GSR slowpath in IOS-XR > http://wiki-eng.cisco.com/engwiki/GsrSlowpathDebuggingXR
					cs-xr12000@cisco.com
					""",

				'ACL':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					Show access-lists {ipv4/ipv6} [acl_name]
					Show access-lists {ipv4/ipv6} [acl_name] hardware ingress location []    // (shows acl information as applied to line card hardware)
					Show access-lists usage pfilter location []           // (Indicates which ACLs are applied to the node and whether they are applied ingress/egress)
					Show access-lists afi-all                                // (shows configured ACL for IPV4 and IPV6 address families)
					Show access-lists maximum detail                        // (shows maximum configurable and current configured number of ACLs)

					Show Techs:
					show tech-support access-lists

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Doc - ACL Commands on XR > https://www.cisco.com/c/en/us/td/docs/ios_xr_sw/iosxr_r3-2/addr_serv/command/reference/ad_r32/ir32acl.pdf
					cs-xr12000@cisco.com
					""",

				'QOS':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show qos acl-deny
					show qos interface [interface name]
					show qos pol-gran
					show policy-map interface []
					show qos interface []


					Traces,debugs and show techs:
					show qos ea-trace
					show qos-ma trace
					show policymgr process trace all                // (trace data for server critical and intermittent failures)
					show policymgr qos trace all
					show app-obj trace
					show policymgr ui trace all
					show tech-support qos pi
					show tech-support qos pd
					debug qos data txm
					debug qos control hardware
					debug qos control rm

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - C12000 QoS > https://wiki.cisco.com/display/GSRTR/C12000+QoS
					gsr-qos-internal
					""",


				'RPL':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show rpl active route-policy detail
					show rpl route-policy
					show rpl route-policy [policy name]

					Traces:
					show rpl trace client-registration reverse
					show rpl trace client lib reverse
					show rpl trace dynamic-registration reverse

					Debugs:
					debug dynuser
					debug policy-repository events
					debug coordinator client gsp
					debug routeaccess docking

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - RPL Component overview and Knowledge base> https://wiki.cisco.com/display/SPRSG/RPL
					cs-xr12000@cisco.com
					""",

				'uRPF':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show cef [IPv4 prefix]
					show cef [IPv4 prefix] hardware egress
					show cef interface [interface name]
					show cef ipv4 hardware egress
					show cef ipv4 hardware egress location [node location]
					show cef ipv4 drops                               //(3  times 30 seconds apart)
					show cef ipv4 drops location [node location]       // (3 times 30 seconds apart)
					show imds interface [interface type] [interface]
					show cef trace

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - C12000 IPv4 URPF Scenarios > https://wiki.cisco.com/display/GSRTR/C12000+IPv4+URPF
					cs-xr12000@cisco.com
					""",

				'NetFlow':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show tech-support netflow
					show flow trace all
					show flow exporter [name]
					show flow internal mgr
					show flow monitor cache location [location]
					show flow monitor location [location]

					Debugs:
					debug flow mgr trace
					debug flow server
					debug accounting netflow
					debug flow perf error
				    debug flow perf trace

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					q-netflow-dev
					cs-12000@cisco.com
					""",

				'E3/E5 Line card':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					admin show sysldr trace all slot [slot]
					admin show controllers fabricq queue detail
					admin show controllers fabric trace
					admin show controllers fabricq drop detail
					admin show controllers fabricq errors detail
					admin show fiad trace
					admin show hw-module fpd location all
					debug cef events

					E3 Hardware:
					show im database interface [interface]
					show im trace
					show cef ipv4 hardware egress location [location]
					show cef ipv4 hardware ingress location [location]
					show cef [prefix] detail
					show netio chains [ type] [ interface number ]

					Traffic:
					show controllers fwd stats location [ node ]
					show controllers pse ingress statistics location [ node ]
					show controllers pse egress statistics location [ node ]
					show controllers egressq qhtl interface [type] [interface number ] location [ node ]   //  (see if head and tail values are moving  )
					show controllers egressq enaq location [ node ]                    // (will show all enable queues for the node)
					show controllers egress bpm [0] [3999] location [ node ]         // (look for ON as indicate backpressure )
					show qos interface [type] [interface number] out/in               // (check both input then output )
					show controllers egressq port [0] [4095] location [ node  ]        // (elegible to send shouls be yes , Bursts can lead to drops)
					show lpts pifib hardware police location [node]
					show controllers egressq carve location [ node ]
					show controllers ingressq carve location [ node ]
					show controllers egressq qmstats 0 location [ node ]                 // (shows red, forced drops per class of service values)
					show controllers ingressq qmstats 0 location [ node ]                // (shows red, forced drops per class of service values)


					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - XBMA - E3 and E5 interface modules > http://wiki-eng.cisco.com/engwiki/E5_20Hardware_20Debug_20Commands
					Wiki - E5-SPA-IOX overview and Troubleshooting > https://wiki.cisco.com/display/CODCGSR/E5-SPA-IOX?preview=/7020849/7020850/E5_overview.png
					Wiki - E3 Hardware Debug Commands > http://wiki-eng.cisco.com/engwiki/E3_20Hardware_20Debug_20Commands
					cs-xr12000@cisco.com
					"""
                }








dict_NCS5500 = { 'Base Commands': """
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show version
					show inventory
					show diag
					show log
					show install log
					show redundancy
					show context
					admin show environment all
					show run
					show configuration commit list
					show proc blocked location all

                    // ( Enter into admin to run admin commands with any pipe filters )
					admin show run
					admin show configuration commit list
					admin show install active sum
					admin show platform
					admin show inventory chassis
					admin show inventory
					admin show led
					admin show diag
					admin show hw-module fpd
					show reboot history location []

                    Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					TechZone -Getting Started with the NCS5500 NCS-5500 (Fretta)  > https://techzone.cisco.com/t5/NCS-5000-5500/Getting-Started-with-the-NCS5500-NCS-5500-Fretta/ta-p/902846
					Cisco Docs - NCS 5500 Deep Dive >  https://cisco.app.box.com/s/drshqly9xqz1tmmec6wv7k5kft0a515q
					Wiki - NCS 5500 Debugging > https://wiki.cisco.com/display/FRE/Debugging+Issues+on+Fretta#DebuggingIssuesonFretta-BundleIssue-Logs/Traces
					Wiki - NCS 5500 Debugging Broadcom > https://wiki.cisco.com/display/FRE/Fretta+Debugging#FrettaDebugging-BroadcomTroubleshooting
					Wiki - CDETS Component  > https://wiki.cisco.com/display/FRE/Component+to+file+DDTS
					TechZone - Engineering > https://techzone.cisco.com/t5/IOS-XR-PD-NCS5500-Coherent-and/bd-p/IOS_XR_PD_NCS5500_Coherent_and_MACSec_Eng
					cs-ncs5500@cisco.com
					"""
				,
				'Broadcom Diagshell':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show controllers fia diagshell "[ bcm command goes here ]" location  [ location where this needs to be executed ]
					BCM commands: //( !! diagshell is used in various troubleshooting sections, if unsure of the command test lab environment first )
					show counters //(  Interface counters )
					show Counters Full //( Displays the MIB counters per interface )
					show unit // ( Shows the Chip architecture number and version )
					show features //( Shows the features configured on the NPU. With the all option it show all possible features )
					diag counters graphical cdsp //( graphical diagram of summary counters (include core info) )
					diag counters nz //( dump of most of the hardware register counters (non zero) )
					diag pp Frwrd_Decision_Trace //( Basic forwarding info for last frame )
					diag pp Received_Packet_Info //( Last packets dumped )
					diag last //( Nicer format of the last packet seen )
					diag pp Parsing_Info //( Last packet information from parser )
					diag pp TERMination_Info //( The programs used for termination )
					diag pp TRAPS_Info //( Last trap info.)
					diag pp ENCAP_info //( Last packet encapsulation information )
					diag pp Frwrd_Lkup_InfoLast //( Fwd lookup keys results and other info )
					diag pp Ing_Vlan_Edit_info //( Last packet Information in Ingress Vlan Edit )
					diag pp PKT_associated_TM_info //( Last packet FID information )
					diag pp DB_LEM_lkup_info //( Last v4 unicast lookup information )
					diag pp FLP_DumpProgram //( indicatore dump )
					gport //( dumps all the ports with corresponding gport and queue info "
					PBMP //( dumps different port bitmaps that can be used in bcm api. )
					ports //( dumps various ports information with link states, loopback, STP and more )
					LISTmem //( Displays all tables )
					Listreg //( Displays all registers )
					config //( Dump the SOC properties )
					cosq conn ing //( display all the voq/connectors/fapid on ingress )
					cosq conn egr //( display all the voq/connectors/fap-id on egress )
					diag cosq voq id=[ number ] detail=1 //( display the programming of specific VoQ displaying all the info including tail drop/wred info/VSQ info etc
					diag cosq qpair egq  //( qpair - display qpair related diagnostics )
					diag cosq qpair egq ps=id //( egq - display egq diagnostics )
					diag cosq qpair e2e //( display e2e diagnostics )
					diag cosq qpair egq ps=id //( ps= - display a graphical representation of the port scheduler in E2E associated with port )
					diag egr //( display egress congestion statistics, also shows all the port, pp_port, qpair, queue stats )
					diag pp sig show=all //( dump the signals in a parsed format )
					SwitchControl //( List features which can be enabled and the current state. ** This crashes on 6.4.5 Jericho" )

					BCM Jericho Only:
					kbp kaps_show //( Dump the LPM table (KAPS) )
					diag pp Kaps_LKuP_info_get //( Get the last LPM lookup )
					diag pp elb //(Display ECMP Load-Balancing information (ECMP group, chosen FEC ID, key) )
					show controllers fia trace brcm-? // ( Where to see the BCM Errors, logs )

                    Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					https://wiki.cisco.com/display/FRE/Broadcom+debug#Broadcomdebug-Helpfulaliasandshellfunctions
					TechZone - Engineering > https://techzone.cisco.com/t5/IOS-XR-PD-NCS5500-Coherent-and/bd-p/IOS_XR_PD_NCS5500_Coherent_and_MACSec_Eng
					cs-ncs5500
					"""
				,
				'Interface':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show logging
					show im database location all
					show interfaces
					show platform vm // ( Check if VM is up )
					show controllers fia trace initialization location [ ]  //( Check NPU are up )
					show controllers optics [ line numer ] //( check that the optics are in service, no alarm, power, Faults or other alarms )
					show controllers npu voq-usage interface [ type ] [ interface number ] instance all location [ ]  //( Check if NPU know about the interface )
					show im data brief interface [ type ] [ interface | bundle number ] location [ ]    //( Check interface manager IM is aware of the interface. should be a handle ID and up )
					show interfaces [ type ] [ interface | bundle number ] brief  //( check they are up up and active active if part of a bundle )

					show arp //( check for hardware entries for each interface type and arp is up )
					show ether-ea interface [ type ] [ interface number ] location [ ] //( Check if ether-ea shows information of the interface. IFM, MAC, MTU )

					Traces:
					show vether-ea trace all location all | file vether-ea.log
					show controllers fia trace all location all | file fia.log
					show ether-ea trace all location all | file ether-ea.log
					show ethernet v-ether trace location all | file ethernet-vether.log
					show ethernet infra trace location all | file ethernet-infra.log
					show ethernet driver trace location all | file ethernet-driver.log
					show grid trace all loc all
					show portmapper trace all location all | file pm.log
					show cef trace location all | file cef.log
					show adjacency platform trace location all | file adj.log
					show tech dpa
					sh tech fabric
					sh tech ethernet interfaces
					show tech ethernet interface
					show tech bundle (Just required for bundle issues )

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - Interface Troubleshooting > https://wiki.cisco.com/display/FRE/Fretta+interface+debug
					TechZone - Engineering > https://techzone.cisco.com/t5/IOS-XR-PD-NCS5500-Coherent-and/bd-p/IOS_XR_PD_NCS5500_Coherent_and_MACSec_Eng
					cs-ncs5500
					"""
				,
				'Bundle':"""
					Useful Commands for Troubleshooting:
					show logging | beg [ month date time ]  //( min 15 mins before and after event , full log if need can be sent to file ]
					sh bundle status brief
					show bundle bundle-[ ether | POS ] [ bundle number ]
					show bundle infrastructure in-progress  //( for Bundles check if bundle replication, status and LACP is up )
					show bundle infrastructure mac-allocation
					show bundle infrastructure counters bfd  //( issue multiple times )
					show bundle | file media:filename

					show bundle status detail | file media:[filename]
					show lacp //( check interfaces for correct states )
					show lacp bundle-[ ether | POS ] [ bundle number ]
					show interfaces bundle-[ ether | POS ] [ bundle number ]

					show interfaces [ bundle member link number ]
					show interface
					show interface brief
					show platform vm
					show im data brief location all
					show im status
					show controllers npu voq-usage interface all instance all location all
					show vether-driver server error location all
					show vether-driver server event location all
					show vether-driver fsm err location all
					show vether-driver fsm event location all

					Trace / show tech:
					show bundle trace process all location all
					show bundle trace all location all
					show vether-ea trace all location all
					show ether-ea trace all location all
					show ethernet v-ether trace location all
					show ethernet infra trace location all
					show controllers fia trace all location all
					show portmapper trace all location all
					show spp trace platform common all location all
					show dpa trace loc all
					show vether-ea trace all loc all

					show tech ethernet interface file media:[filename]
					show tech-support bundles file media:[filename]

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - Bundle Troubleshooting > https://wiki.cisco.com/display/FRE/Bundle+TSG
					TechZone - Engineering > https://techzone.cisco.com/t5/IOS-XR-PD-NCS5500-Coherent-and/bd-p/IOS_XR_PD_NCS5500_Coherent_and_MACSec_Eng
					cs-ncs5500
					"""
				,
			    'QoS':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show policy-map interface [ type ] [ interface number ]     //( PI specific info, including stats )
					show policy-map interface [ type ] [ interface number ] [ input , output , nv ] //( counters for specific direction or satellite/fabric interfaces )
					show qos interface [ type ] [ interface number ] [ input , output ]   //( PD related info for QoS applied on interface )
					show feature-mgr client qos-ea feature summary location [ ]  //( brief list of all the interfaces and attached policy
					show feature-mgr client qos-ea policy summary location [ ] //( brief summary of all the policy-maps known to QoS EA )
					show feature-mgr client qos-ea idb summary location [ ] //( list of all the interfaces where policy is attached )
					show controller npu stats voq ingress interface [ type ] [ interface number ] instance [ NPU instance | all ] location [ ] // ( various options to see per interface
					show controller npu voq-usage interface [ type ] [ interface number ] instance [ NPU instance | all ] location [ ] // ( option to see various TM parameters for given interface on given NPU/LC )
					show controller fia diag [ unit number ] "diag pp rif" location // ( shows "cos_profile" of last packet. A non-zero value means qos-map classification is applied )
					show controller fia diag [ unit number ] "diag pp pkttm" location [ ] // ( shows the TC/DP and VoQ values sent to Ingress TM )
					show qos remote interface[ type ] [ interface number ] location [ ]  // ( displays the queueing related information programmed at the remote voqs. )
					show qos ea trace all location [ ]
					show feat-mgr client qos-ea trace all location [ ]

					Required Triage Commands:
					show log | beg [ date-time during issue ]
					show run  //( includes QoS , interface policy-maps configurations )
					show configuration commit [ list | changes ] //( relevant details on any commits  )
					terminal exec prompt timestamp   //( need time stamps from commands )
					show qos interface  [ type ] [ number ]
					show policy-map interface [ type ] [ number ]
					show qos remote loc []   (for egress policy)
					show bundle bundle-[type] [ bundle number ] // ( If the interface is a bundle, provide complete bundle member information)
					show cds server trace | inc qos
					show cds producer trace location [ ]
					show cds consumer trace location [ ]
					show tech qos platform
					show tech qos pi
					show tech cef platform  // this contains the dpa trace also

                    Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - QoS troubleshooting > https://wiki.cisco.com/display/FRE/Fretta+QoS+Troubleshoot
					TechZone - Engineering > https://techzone.cisco.com/t5/IOS-XR-PD-NCS5500-Coherent-and/bd-p/IOS_XR_PD_NCS5500_Coherent_and_MACSec_Eng
					cs-ncs5500"""
				,
				'BFD PD':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show logging
					show udp brief | include [ip-address-of-bfd-peer]
					show udp detail pcb [pcb got from step in 4]
					show udp statistics

					show bfd session status history int TenGigE 0/4/0/10/3 location [ ]  //( PI command Will give session Discriminator and Reason for session Down )
					show controllers fia diagshell 0 "diag oam ep ID=0x03" location [ ] //( check the BFD session in Broad comm My discr = ID=0xZZ )
					show controllers fia diagshell 0 "dump oamp_rmep_db 3" location [ ]
					show controllers fia diagshell 0 "diag oam counters oamp" location [ ]
					show controllers fia diagshell 0 "diag pp last" location [ ]  //( check the PMF is stamping the right attributes like trap code and oam id )
					show controllers fia diagshell 1 "diag field res 1" location [ ] //( get the PMF entries for BFD )

					attach location [ ]
					dpa_show_ltrace | grep dnxsdk_bfd_get_extended_ip   //( tunnel encap is programmed properly )
					dpa_bfdhwoff_show_client -D > bfdsession.txt  // ( search for the discriminator (My dicr ) in bfdsession.txt and remote_id will be present for that session )
					dpa_show_ltrace | grep bob For BOB sessions check if L2 station add is programmed

					Debug BFD packet drops in pipeline  on bundles:
					sh ether-ea interface bundle-ether 215 location 0/5/CPU0 | in INTF_ID    get the rif of the bundle
					dpa_l3intf_show_client -D | grep -A 60 -B 3 "l3a_intf_id => 0x000006bd" | grep station  get the station_id  programmed in the DPA for that RIF .
					sh controllers fia diagshell 1 "diag pp pi" location 0/4/CPU0  <-- Check the o/p of the parser . Next protocol should be Udp
					sh controllers fia diagshell 1 "diag pp termi" location 0/4/CPU0 Check the packet is terminating or not.  ( ^Mfrwrd_type ipv4_uc )  Indicates the Termination is OK )
					sh controllers fia diagshell 1 "diag pp flp last=1" location 0/4/CPU0 Check what program running in FLP
					sh controllers fia diagshell 1 "diag dbal lp" location 0/4/CPU0 Check what program is running in each stage
					sh ether-ea interface bundle-ether 111 location 0/4/CPU0 | in RIF check the incoming packet rif and lif matching with bundle rif
					sh controllers fia diagshell 1 "diag pp dblif" location 0/4/CPU0 Mservice_    //( type mp vsid: XXX  is the rif of the bundle
					sh controllers fia diagshell 1 "diag pp rif" location 0/4/CPU0    Last packet RIF used: 1646  <-- Bundle rif
					sh controllers fia diagshell 1 "diag pp lif_show gl=1 type=out id=0x11813" location 0/4/CP   check the the EEDB entry for the bfd ip Tunnel id=0x ( MSB of the tunnel id)

					PI related commands:
					show bfd
					show bfd client
					show bfd client history
					show bfd [ipv4 | ipv6] session
					show bfd session detail
					show bfd session detail interface [ type ] [ number ]
					show bfd all session detail location []
					show bfd all session status detail location []
					show bfd all session status history location []
					show bfd counters
					show bfd counters packet interface [ type ] [ number ]
					show bfd counters all packet interface [ type ] [ number ]
					show bfd counters all packet invalid location []
					show bfd statistics private location []
					show bfd counters packet private detail location []
					show lpts pifib hardware static-police location []

					BFD over Bundles:
					show bfd counters ipv4 packet interface [ type ] [ number ] //on all bundle members, Check if both sides sending BFD packets.
					show bfd bundles echo detail location []
					show bfd bundles detail location []
					show bfd all session detail //The session type field should say RTR_BUNDLE

					Debugs/show-tech/traces:
					show tech-support routing bfd
					show tech bundles  //for BFD over bundles
					show tech-support cef platform
					show tech-support dpa
					show tech-support bfdhwoff

					show bfd trace fsm location []
					show bfd trace location []
					Show socket trace process udp
					Show udp trace

					debug bfd [ process | error | lib | client-api ]
					debug bfd trace bfd location []

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - BFD Session down Troubleshooting > https://wiki.cisco.com/display/FRE/How+to+Debug+BFD+Session+going+Down+on+Fretta
					Wiki - BFD packet path > https://wiki.cisco.com/display/FRE/Fretta+BFD++Packet+path+Wiki
					TechZone - Engineering > https://techzone.cisco.com/t5/IOS-XR-PD-NCS5500-Coherent-and/bd-p/IOS_XR_PD_NCS5500_Coherent_and_MACSec_Eng
					cs-ncs5500
					"""
				,
				'CFM':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version
					show run ethernet cfm //( show cfm configuration on this router )
					show ethernet cfm local maintenance-points //( Verify CFM Operation )
					show ethernet cfm local meps
					show ethernet cfm peer meps [ interface [type] [ number ] | errors]  //( looks for errors, up/dn timer )
					show ethernet cfm peer meps detail [ errors | crosscheck ]
					show ethernet cfm ccm-learning-database [ location ]
					show controllers fia diagshell [ np number ] "diag oam ep [id=<ep id>]" location [ ]
					show spp node-counters location [ ] //( show packet counters, punted, classified, injected, issue multiple times )

					LC CPU command:
					run attach 0/[ slot ]/cpu0
					dpa_cfmofflmep_show_client -D | grep -C 10 [if handle]

					EVPN verification:
					show bgp neighbors //( Verify BGP Operation )
					show l2vpn xconnect //( Verify L2VPN Operation )

					CFM Ping/Traceroute:
					ping ethernet cfm domain [ domain name ] service [ service name ] mep-id [ target ] source mep-id [ source ] interface [ type ] [ numeber ] //( Loopback (Ping))
					traceroute ethernet cfm domain [ domainname ] service [ service name ] mep-id [ target ] source mep-id [ source ] interface [ type ] [ number ] //( Linktrace (Traceroute) )

					Debugs:
					debug ethernet cfm support
					debug ethernet cfm packets [interface [] | packet-type []]
					debug ethernet cfm protocol-state

					Traces:
					show dpa trace location []
					show dpa trace location [] | in cfm
					show spio platform hw-offload trace location []
					show ethernet cfm platform trace location []
					show spio platform offload client-lib trace location []
					show spio platform offload lookup trace location []
					show portmapper trace all location []
					show spp trace platform common <all | error> location []
					show controllers fia trace brcm-error location []


					Show Tech:
					show tech dpa location <>
					show tech-support ethernet protocols oam

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					TechZone - NCS5500 CFM Troubleshooting > https://techzone.cisco.com/t5/NCS-5000-5500/CFM-implementation-adn-Troubleshooting-on-NCS550x/ta-p/1071586
					Wiki - CFM Debugging > https://wiki.cisco.com/display/FRE/CFM+Debugging
					Wiki - CFM Function Specs > https://wiki.cisco.com/pages/viewpage.action?pageId=84591118
					TechZone - Engineering > https://techzone.cisco.com/t5/IOS-XR-PD-NCS5500-Coherent-and/bd-p/IOS_XR_PD_NCS5500_Coherent_and_MACSec_Eng
					cs-ncs5500
					"""
				,
				'Control Ethernet':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					admin show controller switch ? //( for all option under switch )
					admin show controller switch reachable //( for a list of all switch and location )
					admin show controller switch summary location [ ] | ? //( list of all loactions and shows where switch ports are connected )
					admin show controller switch statistics location [ ] //( shows counters , issue multiple times )
					show controller switch bridge statistics location [ switch location ] //( dicards, drop, cogestion counters )

					attach location [ ]
					run esd_mgmt_local  //( shows hardware available and connected status EOBC )
					select EPC-SW    //( use select command to change to a different switch , show details about EPC )
					show policing stats  //( will show you stats and if there is any drops )
					quit //( exit back to sys admin )

					show tech-support control-ethernet

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - Control Ethernet Overview > https://wiki.cisco.com/display/FRE/Fretta+Control+Ethernet+High+Level+Approach
					Wiki - Control Ethernet Traffic Classification > https://wiki.cisco.com/display/FRE/Classification+of+traffic+for+Fretta
					Wiki - Getting Started NCS5500 > https://techzone.cisco.com/t5/NCS-5000-5500/Getting-Started-with-the-NCS5500-NCS-5500-Fretta/ta-p/902846#anc6
					Wiki - NCS5500 Control Ethernet Policing Marvell Switch > https://wiki.cisco.com/display/FRE/Fretta+Control+Ethernet+Policing+for+Marvell+Switches
					Wiki - NCS5500 Control Ethernet Queuing Marvell Switch > https://wiki.cisco.com/display/FRE/Fretta+Control+Ethernet+Tx+Queuing+for+Marvell+Switches
					Wiki - Control Ethernet Policing Broadcom Switch > https://wiki.cisco.com/display/FRE/Fretta+control+ethernet+Policing+on+Broadcom+switches
					TechZone - Engineering > https://techzone.cisco.com/t5/IOS-XR-PD-NCS5500-Coherent-and/bd-p/IOS_XR_PD_NCS5500_Coherent_and_MACSec_Eng
					cs-ncs5500
					"""
				,
				'Multicast':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					Traffic Dropped at the First Hop Router:
					show mrib route summary  // ( Verify the number of routes / show pim topology summary / show mfib hardware route summary commands )
					show mrib route detail //( Verify if the incoming and outgoing interfaces are as expected for routes, note FGID number )
					show interface [ type ] [ number ] | inc packets //( packets are being received and sent on outgoing incoming interfaces )
					show mrib fgid info [ fgid number ] //( NPU instance , corresponding to the NPU of the outgoing interface ]
					show controllers npu vpq-usage interface [ type ] [ number ] instance [ NPU number ] location [ ]  //( shows interface for NPU )
					admin show controller fabric fgid information id [ fgid number ] detail //( fabric side, binary bitmap for FGID, LC has 6 bits for 6 NPUs. Shows LC and NPU for FGID belongs )
					show controllers fia diagshell [ npu number ] "diag counters g cdsp" location [ ] //( Ingress, Check NIF_PACKET_COUNTER, ENQ_DSCRD_PKT_CNT )
					show controllers fia diagshell [ npu number ] "kbp kaps show" location [ ]  //( Check the number of entries present and the FLP value )
					show controllers fia diagshell [ npu number ]  "diag pp termi" location [ ] //( Check if the frwd_type is ipv4_mc )
					show controllers fia diagshell [ npu number ] "diag dbal lp" location [ ] //( Check source IP is proper and if the result is non-zero FEC value )
					show controllers fia diagshell [ npu number ] "diag pp sig order=little block=IRPP " location [ ] //( entire IRPP block from input to output, FEC results )
					show controllers fia diagshell [ npu number ] "diag pp fdt" location [ ] //(  check if the packets are dropped owing to RPF failure, look for mc_ecplicit_rpf_fail )

					FH functionality:
					show controller npu stats traps-all instance all location [ ] | inc MC  //( PMF stage, the very first entry programed in TCAM is the special FEC 0x4500, action Trap)
					show spp node-counters //(  PUNT IPV4MC_DO_ALL_BUT_FWD=SNOOP, PUNT IPV4MC_DO_ALL=TRAP,  sends to PIM ,encapsulate packet sends via unicast to RP )

					Triage Collection:
					show mrib fgid info summary
					show mrib fgid info all
					show mrib fgid info all standy
					show mrib [ ipv6 | ipv4 ] route detail
					show mfib hardware route summary location [ ]
					show mfib hardware route detail location [ ]
					show mfib [ ipv6 | ipv4 ] hardware route detail location [ ]
					show mfib [ ipv6 | iov4 ] route location [ ]
					show pim neighbors
					show pim topology summary
					show controllers fia diagshell 0 "diag counters g" location [ ]
					show dpa resources ipmcroute location [ ]
					show dpa resources ipmcolist location [ ]

					Traces/Show techs:
					show mrib platform trace all location [ ]
					show mfib hardware trace all location [ ]
					show mfib trace rev location [ ]
					show mfib hardware trace route rev location [ ]
					admin show controller fabric fgid trace prog-info location [ RP ]  |  i "fgid 36723"  //( goto to admin mode first )
					show mfib hardware trace idb location [ ]  | include "Bundle Idb not yet created"
					attach location [ ]
					bcmd 0 "diag alloc FEC direct=1 from=17387 to=17395"
					show controllers fia diagshell [ npu ] "diag pp fdt core=1" location [ ]
					show controllers fia diagshell [ npu ] "kbp kaps_show" location [ ]
					attach location [ ]
					dpa_ipmcolist_show_client -c

					All MC tables dump in  DPA on all LC:
					attach location [ ]
					dpa_ipmcolist_show_client -D > lc0ipmcolist.dump
					dpa_ipmcroute_show_client -D > lc0ipmcroute.dump
					dpa_ip6mcroute_show_client -D > lc0ip6mcroute.dump

					fia Trace on all LC:
					attach location [ ]
					fia_show_ltrace -A > lc0fia.trace

					sh tech multicast  (PI Show tech)
					show tech dpa location [ all LC ]

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					https://wiki.cisco.com/display/HEROBU/Fretta+Multicast
					https://wiki.cisco.com/display/FRE/Current+handling+of+Multicast+packets+in+fretta
					https://wiki.cisco.com/display/FRE/Debugging+ingress+processing+of+packets
					https://wiki.cisco.com/pages/viewpage.action?pageId=71331662
					https://wiki.cisco.com/display/FRE/Multicast+Wiki
					fretta-mcast-dev@cisco.com
					"""
				,
				'Packet Drops':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show interfaces [type ] [ interface number ] // ( show input and output packet drops outside of Packet processing layer in NPU,  run on all links if in a bundle )
					show controllers npu voq-usage interface [ type ] [ interface number ]   // ( Find NPU where interface is hosted , pp port #,  )
					show controllers fia diagshell [ NPU ID ] "diag last" location []  // ( Capture packet on the NPU where the interface is hosted. Look for pp port to find packet )
					show controllers fia diagshell [ NPU ID ] "diag counter g c" location []  //( NPU and core / on outgoing or incoming interface shows data path counters )
					show controller npu stats counters-all instance [ NPU ID ] location  [ NPU Location | all ]  // ( per stage counters, Stats from each processing stage from NPU )
					show controllers npu stats traps-all instance [ NPU ID ] location  [ NPU Location | all ]  //( if a packet drops or sent to CPU, If a packet is trapped to CPU )
					show spp node-counters location [] //( host bound packets not marked drop in trap counters , check SPP counters for any drops )
					show controllers npu stats voq base 1112 instance [ NPU ID ] location  [ NPU Location | all ] //( Get voq id from voq-usage command, If packet is transit                                                                                                                                                                        and you don't see any traps incrementing then, look into VOQ stats )
					show lpts pifib hardware police location [] // ( hw supported flow types and their configured policer rates )
					show lpts pifib hardware entry brief location []   // ( look for any drops )
					show captured packets [ ingress | egress ] location []  // (  packet dropped in the PP pipeline )
					show controllers fia diagshell [ NPU ID ] "diag pp last detailed" location []  //( Details of packet path for any packet, match PP port in the output to
																																					ensure the packet is received on the interface of interest )
					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - NCS5500 pactet Drops > https://wiki.cisco.com/display/FRE/Fretta+packet+drop
					Wiki - NCS5500 LPST > https://wiki.cisco.com/display/FRE/Fretta+LPTS+-+Local+Packet+Transport+Servieces
					Wiki - NPU Packet Drops > https://wiki.cisco.com/display/FRE/NPU+Controller
					TechZone - Engineering > https://techzone.cisco.com/t5/IOS-XR-PD-NCS5500-Coherent-and/bd-p/IOS_XR_PD_NCS5500_Coherent_and_MACSec_Eng
					cs-ncs5500
					"""
				,
				'ACL':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show run
					show version

					PI ACL:
					show access-lists summary //( Summary of all ACLs/ACEs that are configured
					show access-lists afi-all // ( ACL/ACE configuration info for both IPv4 and IPv6 )

					PD ACL/pfilter :
					show access-lists [ ipv4 | ipv6 ]  [ acl_name ] hardware[ ingress | egress ]  location [ ]   // ( PD config (counters only) )
					show access-lists [ ipv4 | ipv6 ]  [ acl_name ] hardware [ ingress | egress ] detail location [ ] // ( PD config (detailed dump of config from DPA))
					show access-lists [ ipv4 | ipv6 ]  usage pfilter location [ ]   // ( ACL usage by pfilter )

					PD FM (Feature Manager):
					show feature-mgr client pfilter-ea idb sum location [ LC ]  // ( summary of interface config for ACLs )
					show feature-mgr client pfilter-ea feature-info sum location [ LC ]  //( summary of ACL config per interface )
					show feature-mgr client pfilter-ea feature-info feature-name [ acl_name ] direction [ ingress | egress ] lookup [ ipv4|ipv6 ] int [ type ] [ number ] location [ ]
					// ( FM database contents for ACL )

					TCAM :
					show controllers npu internaltcam location [ ]  //(  Internal TCAM usage )
					show controllers npu externaltcam location <lc>   // ( External TCAM usage )
					show controllers npu resources stats instance <npu> location <loc> // ( Statistics resources (ACL, etc..)

					Broadcom commands:
					show controllers fia diagshell 0 "diag field last core=0" location <location> // ( View contents of the last packet received )
					show controllers fia diagshell <npu> "l2 show" location <LC> // ( View MAC entries in L2 bridges )
					show controllers fia diagshell <npu> "diag counters g" location <LC> // ( Jericho ingress/egress traffic stats, may help identify traffic being forward/discarded by ACLs, etc.)
					show controllers fia diagshell <npu> "diag pp pi core=0"   location <LC> // ( View vlan tag info on last packet pp, hdr_type, protocol, initial_vid )
					show controllers fia diagshell <npu> "diag pp last core=0" location <LC> // ( View Last Packet PP, core = 0 or 1 )
					show controllers fia diagshell <npu> "diag pp kbp iterator iterate=ACL" location <LC> //( Dump external TCAM entries for hybrid ACL )
					show controllers fia diagshell 0 "diag pp kbp print" location <LC> // ( External TCAM usage )

					show controller fia trace all location [ ]
					show pfilter-ea ipv4 trace all location [ ]
					show pfilter-ea ipv6 trace all location [ ]
					show pfilter-ea ethernet-services trace all location [ ]
					show feature-mgr client pfilter-ea trace all location [ ]
					show dpa trace location [ ]
					show tech-support
					show tech-support access-lists [ ipv4 | ipv6 | ethernet-services ]

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Wiki - ACL > https://wiki.cisco.com/display/FRE/ACL+Wiki
					Wiki - ACL XRF > https://wiki.cisco.com/display/FRE/ACL+XTF+Wiki
					TechZone - Engineering > https://techzone.cisco.com/t5/IOS-XR-PD-NCS5500-Coherent-and/bd-p/IOS_XR_PD_NCS5500_Coherent_and_MACSec_Eng
					cs-ncs5500"""
				,
				'AIB':"""
					Useful Commands For Troubleshooting: //( Some commands syntax could vary according to platform or version)
					ARP/ND (Adj Producer):

					Check ARP/ND entries exists for given Nexthop IPv4/v6 addresses
					show arp
					show ipv6 neighbors

					To debug any ARP/ND issues:
					show tech-support arp / show tech-support ipv6 nd
					show arp trace / show ipv6 nd trace
					debug arp / debug ipv6 nd

					AIB:
					Check Adj database
					show adj [interface] detail
					show adjacency internal detail location []
					show adj [interace] detail hardware location []   (for Tx/local adjacencies)
					show adj [interace] remote detail hardware location []   (for Rx/remote adjacencies)

					To debug any AIB issues:
					show tech-support cef  (PI)                   //(collects show adj traces)
					show tech-support cef  platform (PD)   //(collects show adj platform traces)
					show adjacency trace all (PI)
					show adjacency platform trace (PD)
					show adjacency producer/consumer
					show tech aib

					FIB (consumer for local LC, producer for remote LC):
					Fretta FIB  (Use Fretta FIB debug page)

					BMA (external Mgr):
					show bundle status
					show bundle load-balancing
					show bundle trace process adjacency    (debugging)
					debug bundle infrastructure adjacency   (debugging)

					PPINFO/CDS (Adjacency Distribution):
					show ppinfo producer trace all        //(ppinfo producer is FIB-NH lib)
					show ppinfo consumer trace all      //(ppinfo consumer is AIB lib)
					show cds producer trace                //(cds producer is FIB-NH lib)
					show cds consumer trace             //  (cds consumer is AIB lib)
					show cds proxy trace                     // (proxy to interact with CDS server for consumer side)
					show cds server trace                    // (Server resides in RP to store and maintain CDS labels)
					debug ppinfo producer/consumer
					debug ads producer/consumer/proxy/server

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					https://wiki.cisco.com/display/FRE/Fretta+AIB
					"""
				,
				'FABRIC':"""
					Useful Commands for Troubleshooting: //( Some commands syntax could vary according to platform or version)
					show log | inc FABRIC
					show platform

					show controllers fia statistics instance [0-15, all] location []   //( issue multiple times look for errors and rx/tx increments based on expected traffic )
					show controllers fia driver location [all] // ( asic state should be normal - NRML )
					show controllers fia link-info rx 0 35 flap instance [ asic 0-15 | all ] location []  | ex DN //( Use of ex DN will only show up links, look for errors ]
					show controllers fia link-info tx 0 47 instance 0 location 0/2/cpu0
					show controllers fia diagshell [fia number] "fabric reachability [destination number ]" location []  //( shows reachability from a fia asic on a LC, all 36 should be available )
					show controllers fia diagshell [fia number] "fabric link [ link number ]" location []
					show controllers fia link-info rx [ Start link number] [ End link number ] topo instance  [ asic 0-15 | all ] location []  //( for start and stop use same number to focus on 1 link , look
																																																		for flags for reasons a link could be down )
					show controller fia diagshell [ 1-63 ] "show patches" location []
					show asic-errors fia [number] all location [] //( LC FIA asic errors, get asic instance 0-4 number from above command or a sys log message)
					show asic-errors fia [number] nonerr location []
					show asic-errors tcam [ 0-7 ] all location []

					//( admin commands if issued outside of admin mode may have issue with pipe filter, enter admin mode first, then show commands )

					admin show controller fabric health  //( FIA is on LC, SFE is on fabric card)
					admin show controller fabric plane all
					admin show controller fabric fsdb-pla rack 0 //( Fabric destination reachability , p = slots, mask = fia link to SFE fabric , destination R/S/A )
					admin show controller fabric fsdb-pla rack 0 destination [ Asic number from above ]
					admin show controller fabric link port fia tx | inc [0/slot/fia] //( tx to SFE - 36 total )
					admin show controller fabric link port fia tx | inc [0/slot/fia] //( rx from SFE - 36 total )
					admin show controller fabric link port [ fia, s1,s2,s3 ] [rx, tx ] [ all, brief,detail, state, statistics ]
					admin show controller fabric link port [ fia, s1,s2,s3 ] [rx, tx ] statistics brief //( for summary view of errors collect for all and tx and rx )
					admin show controller fabric link port [ fia, s1,s2,s3 ] [rx, tx ] statistics detail //( for details if you see errors from above commands )

					admin show controller fabric sfe fia all
					admin show controller fabric sfe s123 all
					admin show controller sfe driver location 0/FC[0-6] // ( asic state should be normal - NRML )
					admin show controller sfe link-info rx 0 143 flap instance [ asic 0-5 | all ] location [ Fabric LC ]  | ex DN  //( Use of ex DN will only show up links, look for errors ]
					admin show controller sfe link-info tx 0 143 instance  [ asic 0-5 | all ] location [ Fabric LC ]
					admin show controller sfe link-info rx  [ Start link number] [ End link number ] topo instance [ asic 0-5 | all ] location [ Fabric LC ]
					admin show controller sfe diagshell [ asic 0-5 ]"show patches" location [ Fabric LC ]
					admin show processes sfe_driver location [ Fabric LC ]
					admin show processes fsdb_server location [ RP active | standby ]
					admin show processes fsdbagg location [ RP active | standby ]
					admin show processes fgid_mgr location [ RP active | standby ]
					controller fabric plane 0 shutdown  //( in admin config mode use to shut a plane down )

					show controllers fabric trace [ location ] | file disk0:fab_trc_[LC_number].log
					show controllers fia trace all location [] | file disk0:fia_trc_[LC_number].log
					show asic-errors fia trace [ all, api, error, event ]
					show asic-errors tcam trace [ all, api, error, event ]
					show tech fabric [ location ]

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					TechZone - Fretta Basics > https://techzone.cisco.com/t5/NCS-5000-5500/Getting-Started-with-the-NCS5500-NCS-5500-Fretta/ta-p/902846
					TechZone - Fabric Troubleshooting > https://techzone.cisco.com/t5/NCS-5000-5500/NCS-5516-Fabric-Troubleshooting/ta-p/1076733
					TechZone - Fabric Troubleshooitng > https://techzone.cisco.com/t5/NCS-5000-5500/NCS-5508-Fabric-Troubleshooting/ta-p/1061928
					XR Geeks - Fabric materials > http://xrgeeks.cisco.com/?q=content/ncs-5500-troubleshooting-material
					Cisco Docs - NCS5500 Fabric Architecture_debug >  https://cisco.jiveon.com/docs/DOC-1851125
					Wiki - Fabric > https://wiki.cisco.com/display/FRE/Fretta+Fabric
					TechZone - Engineering > https://techzone.cisco.com/t5/IOS-XR-PD-NCS5500-Coherent-and/bd-p/IOS_XR_PD_NCS5500_Coherent_and_MACSec_Eng
					fretta-fabric-dev
					"""

              }


dict_7600 = {'Routing':"""
					Useful Commands For Troubleshooting:  //( Some commands syntax could vary according to platform or version)
					show [ip/ipv6] cef vrf internal
					show mls cef [ip/ipv6] vrf to detail
					show mls cef adjacency entry detail
					show mls cef adjacency flags
					show vlan internal usage // (on RP)
					show l3mgr interface vlan
					show mls vlan-ram

					show mls cef mpls label detail
					show mls rate-limit hw-detail
					show [ip/ipv6] cef vrf platform internal //(may be a long output)

					On RP:
					show ibc
					debug netdr capture rx interface
					show netdr captured-packets
					show mac-address-table detail // (on RP and SP/DFC)
					show idb
					show cef interface internal
					show mls statistics
					show mls cef statistics // (on RP and SP/DFC)
					show ip cef switching statistics
					show int counters
					show int stats
					show int summary
					show int

					//Please see links below for further commands, debugs, and elam capture.

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Jive 7600 Cheat Files > https://cisco.jiveon.com/docs/DOC-1448680
					Wiki 7600 Troubleshooting Guide > https://wiki.cisco.com/display/TSG/7600+Trouble+Shooting+Guide
					Wiki 7600 Troubleshooting Guide IPv4 Routing Forwarding Troubleshooting > https://wiki.cisco.com/display/TSG/7600+Trouble+Shooting+Guide
					cs-7600@cisco.com
					"""
				,
				'IPv6':"""
					Useful Commands For Troubleshooting:  //( Some commands syntax could vary according to platform or version)
					show ipv6 route
					show ipv6 cef
					show ipv6 cef internal
					show ipv6 cef platform internal
					show mls cef ipv6 detail
					show mls cef ipv6 summary

					Useful Debugs:
					debug ipv6 cef [drop|events|hash|packet|receive|table]
					debug ipv6 platform all


					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Jive 7600 Cheat Files > https://cisco.jiveon.com/docs/DOC-1448680
					Wiki 7600 Troubleshooting Guide > https://wiki.cisco.com/display/TSG/7600+Trouble+Shooting+Guide
					Wiki 7600 Troubleshooting Guide IPv6 Routing Troubleshooting > https://wiki.cisco.com/display/TSG/Ipv6+Routing+Troubleshooting+Guide
					cs-7600@cisco.com
					"""
				,
				'MPLS':"""
					Useful Commands For Troubleshooting:  //( Some commands syntax could vary according to platform or version)
					show mpls ldp neighbor
					show mpls ldp binding
					show mpls forwarding-table
					show mpls l2 vc [vcid] detail

					show mpls infrastructure lfd pseudowire pwid detail
					show mls cef mpls label [local label] detail
					show mls cef mpls label [label] detail // if there is recirc label
					show mpls forwarding-table labels <label>
					show mls cef mpls labels <label>

					show mpls l2transport vc
					show mpls l2transport vc detail
					show mpls l2transport summary
					show mpls traffic-eng tunnels tunnel [tunnel number] detail

					Useful Debugs:
					debug mpls l2transport vc ldp
					debug mpls l2transport signaling event
					debug mpls l2transport signaling message

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Jive 7600 Cheat Files> https://cisco.jiveon.com/docs/DOC-1448680
					Wiki 7600 Troubleshooting Guide> https://wiki.cisco.com/display/TSG/7600+Trouble+Shooting+Guide
					Wiki 7600 Troubleshooting Guide MPLS Troubleshooting> https://wiki.cisco.com/display/TSG/7600+MPLS+TSG
					Wiki 7600 Troubleshooting Guide MPLS Troubleshooting IP FRR> https://wiki.cisco.com/display/TSG/MPLS+IP+FRR
					Wiki 7600 Troubleshooting Guide MPLS Troubleshooting TP> https://wiki.cisco.com/display/TSG/MPLS+TP
					Wiki 7600 Troubleshooting Guide MPLS Troubleshooting VPN TTL Programming> https://wiki.cisco.com/display/TSG/MPLS+VPN+-+TTL+programming+in+EARL+and+VPNCAM+usage
					cs-7600@cisco.com
					7600-mpls-queries@cisco.com
					"""
				,
				'Multicast':"""
					Useful Commands For Troubleshooting:  //( Some commands syntax could vary according to platform or version)
					show ip pim neighbor
					show ip mroute [ip]
					show ip mfib [ip][mask] verbose
					show platform software multicast ip capability
					show platform software multicast ip cmfib [ip][mask] ver
					show vlan internal usage | i [vlan]
					show ip pim vrf [vrf] neighbor
					show ip pim mdt
					show ip mfib vrf [vrf] [ip][mask] verbose
					show ip mroute vrf [vrf] [ip][mask] verbose
					show platform software multicast ip cmfib vrf [vrf] [ip][mask] ver
					show platform vpn mapping | i [vrf]
					show platform software multicast ip cmfib vrf [vrf] mdt encapsulation-path [ip][mask] verbose

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Jive 7600 Cheat Files > https://cisco.jiveon.com/docs/DOC-1448680
					Wiki 7600 Troubleshooting Guide > https://wiki.cisco.com/display/TSG/7600+Trouble+Shooting+Guide
					Wiki 7600 Troubleshooting Guide MCAST > https://wiki.cisco.com/display/TSG/7600+MCAST+TSG
					Wiki 7600 Troubleshooting Guide L2 Multicast > https://wiki.cisco.com/display/TSG/L2+Multicast
					Wiki 7600 Troubleshooting Guide MLDP > https://wiki.cisco.com/display/TSG/MLDP
					Wiki 7600 Troubleshooting Guide MVPNv4 > https://wiki.cisco.com/display/TSG/MVPNv4
					Wiki 7600 Troubleshooting Guide MVPNv6 > https://wiki.cisco.com/display/TSG/MVPN+v6
					7600 Troubleshooting Guide Native Multicast > https://wiki.cisco.com/display/TSG/Native+Multicast
					cs-7600@cisco.com
					7600-mcast-team@cisco.com
					c7600-mcast@cisco.com
					"""
				,
				'Tunnels':"""
					Useful Commands For Troubleshooting:  //( Some commands syntax could vary according to platform or version)
					GRE Tunnels:
					show run interface Tunnel [tunnel]
					show run interface [source]
					show vlan internal usage
					show adjacency tunnel [tunnel] internal
					show ip cef [prefix] detail
					show mls cef adjacency

					L2TPv3 Tunnels:
					show xconnect all
					show xconnect all detail
					show xconnect interface [interface] detail
					show l2tun session
					show l2tun session brief
					show l2tun socket
					show l2tun session all
					show l2tun tunnel all
					show l2tp counters // 3 Times 30 seconds apart
					show ssm id
					show fm interface [interface]
					show platform l2tpv3 disp-tbl
					show platform l2tpv3 imp-tbl
					show platform l2tpv3 session-id [id] // get id from previous command

					L2TPv3 Debug commands:
					debug l2tp [all | *]
					debug xconnect event
					debug xconnect error
					debug acircuit event
					debug acircuit error
					debug acircuit checkpoint
					debug sss event
					debug sss error
					debug sss fsm
					debug ssm cm error
					debug ssm cm event
					debug ssm sm error
					debug ssm sm event
					debug vpdn event
					debug vpdn error
					debug vpdn l2x-event
					debug vpdn l2x-error
					debug atm l2transport

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Jive 7600 Cheat Files > https://cisco.jiveon.com/docs/DOC-1448680
					Wiki 7600 Troubleshooting Guide > https://wiki.cisco.com/display/TSG/7600+Trouble+Shooting+Guide
					Wiki 7600 Troubleshooting Guide Tunnels > https://wiki.cisco.com/display/TSG/Tunnels+Troubleshooting+Guide
					Wiki 7600 Troubleshooting Guide Tunnels HA > https://wiki.cisco.com/display/TSG/7600+Tunnels+HA
					Wiki 7600 Troubleshooting Guide IP GRE Tunnels > https://wiki.cisco.com/display/TSG/IP+GRE+Tunnels
					Wiki 7600 Troubleshooting Guide IPv6 Tunneling over IPv4 Transport > https://wiki.cisco.com/display/TSG/IPv6+Tunneling+over+IPv4+Transport
					Wiki 7600 Troubleshooting GuideL2TPv3 L2 Tunneling Protocol Version 3 > https://wiki.cisco.com/display/TSG/L2TPv3+-+Layer+2+Tunneling+Protocol+Version+3
					Wiki 7600 Troubleshooting Guide Excalibur L2TPv3 Troubleshooting Guide > https://wiki.cisco.com/display/TSG/Excalibur+L2TPv3+Troubleshooting+Guide
					Wiki 7600 Troubleshooting Guide MPLSoGRE > https://wiki.cisco.com/display/TSG/MPLSoGRE
					Wiki 7600 Troubleshooting GuideMPLS VPN over MGRE > https://wiki.cisco.com/display/TSG/MPLS+VPN+over+MGRE
					Wiki 7600 Troubleshooting GuideVRF aware 6RD Tunnels > https://wiki.cisco.com/display/TSG/VRF+aware+6RD+Tunnels
					EDCS-817843 6RD Tunnels Functional & Design Specification > https://docs.cisco.com/share/page/site/nextgen-edcs/document-details?nodeRef=workspace://SpacesStore/96cda636-dfa5-4c7e-9ca8-84a8682fa60e
					EDCS-958400 6RD platform SFS > https://docs.cisco.com/share/page/site/nextgen-edcs/document-details?nodeRef=workspace://SpacesStore/6d1cc884-d3d1-4919-9b0d-0d712f224a5a
					EDCS-792632 6rdPRD > https://docs.cisco.com/share/page/site/nextgen-edcs/document-details?nodeRef=workspace://SpacesStore/a06693b3-b4b6-46a8-9599-c205fc99d8c5
					EDCS-792631 6rdTutorial > https://docs.cisco.com/share/page/site/nextgen-edcs/document-details?nodeRef=workspace://SpacesStore/a59f36b7-9d0d-4da6-9ecb-7e691991025d
					Wiki - 7600 MCAST TSG > https://wiki.cisco.com/display/TSG/7600+MCAST+TSG
					cs-7600@cisco.com
					7600-mcast-team@cisco.com
					"""
				,
				'Feature Manager':"""
					Useful Commands For Troubleshooting:  //( Some commands syntax could vary according to platform or version)

					RP Commands:
					show fm interface
					show fm fie interface
					show fm fie flowmask detail
					show fm fie fidb
					show tcam interface [int] acl in ip detail

					SP Commands:
					show mls acl i2k_svlan
					show mls acl i2k_sidx
					show ip platform software errors

					Useful Debugs:
					debug fm // use ? to view all options

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Jive 7600 Cheat Files > https://cisco.jiveon.com/docs/DOC-1448680
					Wiki 7600 Troubleshooting Guide > https://wiki.cisco.com/display/TSG/7600+Trouble+Shooting+Guide
					Wiki 7600 Troubleshooting Guide Feature Manager > https://wiki.cisco.com/display/TSG/Feature+Manager
					Wiki 7600 Troubleshooting Guide DHCP Snooping > https://wiki.cisco.com/display/TSG/DHCP+Snooping
					Wiki 7600 Troubleshooting Guide Network Address Transalation > https://wiki.cisco.com/display/TSG/Network+Address+Translation
					Wiki 7600 Troubleshooting Guide PACL VACL RACL > https://wiki.cisco.com/display/TSG/PACL+VACL+RACL
					Wiki 7600 Troubleshooting Guide PBR > https://wiki.cisco.com/display/TSG/PBR
					Wiki 7600 Troubleshooting Guide SLB > https://wiki.cisco.com/display/TSG/SLB
					Wiki 7600 Troubleshooting Guide WCCP > https://wiki.cisco.com/display/TSG/WCCP
					cs-7600@cisco.com
					7600-fm-india@cisco.com
					"""
			,
				'QOS':"""
					'Useful Commands For Troubleshooting:  //( Some commands syntax could vary according to platform or version)
					show class-map
					show running class-map
					show policy-map
					show running policy-map
					show policy-map intreface <interface>
					show hqf interface

					Useful Debugs:
					debug qos capability
					debug qos events
					debug qos service-policy lifecycle
					debug qos service-policy stats
					debug cpl ppcp infra
					debug cpl ppcp client
					debug cpl ppcp stats
					debug hqf client
					debug hqf infra

					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Jive 7600 Cheat Files> https://cisco.jiveon.com/docs/DOC-1448680
					Wiki 7600 Troubleshooting Guide> https://wiki.cisco.com/display/TSG/7600+Trouble+Shooting+Guide
					Wiki 7600 Troubleshooting Guide QOS> https://wiki.cisco.com/pages/viewpage.action?pageId=3980229
					cs-7600@cisco.com"""
				,
					'Netflow':"""
					Useful Commands For Troubleshooting:  //( Some commands syntax could vary according to platform or version)
					show mls nde
					show cef interface internal
					show fm interface
					show fm interface internal
					show fm fie flowmask
					show l3-mgr flowmask
					show mls netslow
					show mls netflow table-contention
					show mls netflow aging
					show mls netflow creation
					show mls netflow aggregration flowmask

					Useful Debugs:
					debug l3-mgr flowmaks
					debug l3-mgr interface
					debug l3-mgr events
					deub fm netflow all


					Support Links: //( links can become obsolete at any time, send feedback on commands and links to help maintain accuracy )
					Jive 7600 Cheat Files > https://cisco.jiveon.com/docs/DOC-1448680
					Wiki 7600 Troubleshooting Guide > https://wiki.cisco.com/display/TSG/7600+Trouble+Shooting+Guide
					Wiki 7600 Troubleshooting Guide Netflow > https://wiki.cisco.com/display/TSG/Netflow#Netflow-6.ShowCommands
					Cisco 7600 Netflow PPT > http://wwwin.cisco.com/sptg/sprtg/earbu/products/7600/files/Cisco-7600-netflow.ppt
					cs-7600@cisco.com
					7600-fm-india@cisco.com"""
				}



dict_NCS5000 = {'To be added':"N/A"}

dict_NCS6000 = {'To be added':"N/A"}

dict_eXR = {'To be added':"N/A"}

not_found = "We are sorry, there is still no content for this platform/technology. You can use the link bellow to suggest content for this feature. Thank you."
