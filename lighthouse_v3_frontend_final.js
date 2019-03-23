//jshint laxcomma: true, node: true, indent: false, camelcase: false, expr: true
"use strict";
/***

Provides technical guidance on a case. The user can select if they need a suggestion based on the latest problem description or manually select the technology they need help with. The script will provide a list of commands to collect as well as technical wikis or techzone for that topic.
Last updated Dec 12, 2018
***/

(function($) {

var _debug_ = true;
var _debug_prefix_ = "cs1_Lighthouse_v3.0:";
var LOG = _debug_ ? console.log.bind(console,_debug_prefix_) : function () {};


var caseDetails = BJB_CS1_HELPER.getCaseDetails();
var c3SRNumber = caseDetails["C3SRNumber"];
var right_window  = BJB_CS1_HELPER.getRightFrame();
var main_window = BJB_CS1_HELPER.getMainFrame();
var lh_main_html = '<img src="https://i.imgur.com/IwzMdMJ.jpg" alt="" style="vertical-align:middle;"><a id="LMenuLink" href="" style="color:white" title="Click here to receive technical advice on your case.">\
    <h1>Lighthouse : Click to get help on this case.</h1></a> <div id="LighthouseOverlay1"><div id="LighthouseFrame1"><div id="LighthouseInnerFrame1"></div></div></div>';


function PaneOpen(html){
  var modal = main_window.picoModal({
      content: html,
      overlayClose: false,
      closeButton: false,
      width: "85%",
  });
  return modal;
}


function PaneOpenErr(html){
  var modal = main_window.picoModal({
      content: html,
      overlayClose: true,
      closeButton: true,
      width: "75%",
  });
  return modal;
}


function displayResults(input) {
    var modal = {};
    modal = PaneOpen(input);
    modal.afterCreate(function(modal){
        modal.modalElem().getElementsByClassName("thumbs-up")[0].addEventListener('click', function(){
            var platf = $("#Lighthouse_select_pl").find('option:selected').text();
            var tech = $("#Lighthouse_select_tech").find('option:selected').text();
            LOG("Platform and technology for feedback are :" + platf + " + " + tech);
            BJB_CS1_HELPER.runBdbTask(
                "lighthouse_v3_statistics",
                {
                    'caseid': c3SRNumber,
                    'action' : 'save_entry',
                    'platform': platf,
                    'technology': tech,
                    'feedback' : "Like"
                },
                function (result) {
                    LOG("AJAX call was successful.Feedback sent");
                },
                function (xhr, ajaxOptions, thrownError) {
                    LOG("ERROR!");
                    LOG(xhr.status)
                    LOG(xhr.responseText)
                    LOG(thrownError)
                    return [];
            });
        });
        modal.modalElem().getElementsByClassName("thumbs-up")[0].addEventListener('click', modal.close);
        modal.modalElem().getElementsByClassName("thumbs-down")[0].addEventListener('click', function(){
        var platf = $("#Lighthouse_select_pl").find('option:selected').text();
        var tech = $("#Lighthouse_select_tech").find('option:selected').text();
        LOG("Platform and technology for feedback are :" + platf + " + " + tech);
        BJB_CS1_HELPER.runBdbTask(
            "lighthouse_v3_statistics",
            {
                'caseid': c3SRNumber,
                'action' : 'save_entry',
                'platform': platf,
                'technology': tech,
                'feedback' : "Dislike"
            },
            function (result) {
                LOG("AJAX call was successful.Feedback sent");
            },
            function (xhr, ajaxOptions, thrownError) {
                LOG("ERROR!");
                LOG(xhr.status)
                LOG(xhr.responseText)
                LOG(thrownError)
                return [];
            });
        });
        modal.modalElem().getElementsByClassName("thumbs-down")[0].addEventListener('click', modal.close);
    });
    modal.afterClose(function (modal) {
        LOG("Modal Closed");
        $("#Lighthouse_select_pl").val("0");
        right_window.Lighthouse_select_tech.style.display = 'none';
        right_window.Lighthouse_select_pl.style.display = 'none';
    });
    modal.show();
  };


function displayResultsErr(input) {
    var modal = {};
    modal = PaneOpen(input);
    modal.show();
  };


var cs1_Lighthouse_v3 = function(){

    var Lighthouse_Main = document.createElement('div');
        Lighthouse_Main.id = 'Lighthouse_Main';
        Lighthouse_Main.style.textAlign = 'left';
        Lighthouse_Main.style.backgroundColor = "rgb(121, 180, 205)";
        Lighthouse_Main.style.color = 'white';
        Lighthouse_Main.innerHTML = lh_main_html;
        Lighthouse_Main.style.display = 'none';
        right_window.document.getElementById('TLGPage').appendChild(Lighthouse_Main);


    var Lighthouse_Loading = document.createElement('div');
        Lighthouse_Loading.id = 'Lighthouse_Loading';
        Lighthouse_Loading.style.textAlign = 'left';
        Lighthouse_Loading.style.backgroundColor = "rgb(172, 215, 230)";
        Lighthouse_Loading.style.color = 'black';
        Lighthouse_Loading.innerHTML = "Loading...";
        Lighthouse_Loading.style.display = 'none';
        right_window.document.getElementById('Lighthouse_Main').appendChild(Lighthouse_Loading);


    var Lighthouse_select_pl = document.createElement('select');
        Lighthouse_select_pl.id = 'Lighthouse_select_pl';
        Lighthouse_select_pl.style.textAlign = 'left';
        Lighthouse_select_pl.style.width = "100%";
        Lighthouse_select_pl.style.display = 'none';
        right_window.document.getElementById('Lighthouse_Main').appendChild(Lighthouse_select_pl);


    var Lighthouse_select_tech = document.createElement('select');
        Lighthouse_select_tech.id = 'Lighthouse_select_tech';
        Lighthouse_select_tech.style.textAlign = 'left';
        Lighthouse_select_tech.style.width = "100%";
        Lighthouse_select_tech.style.display = 'none';
        right_window.document.getElementById('Lighthouse_Main').appendChild(Lighthouse_select_tech);


    var link = right_window.document.getElementById("LMenuLink");
        link.onclick = function() {
            right_window.Lighthouse_select_pl.style.display = '';
            return false;
        }

    BJB_CS1_HELPER.runBdbTask(
        "lighthouse_v3_backend",
        {
            'action': 'get_platform_list'
        },
        function (result) {
            LOG("AJAX call was successful. Platform list received");
            LOG(JSON.stringify(result));
            var platform_html = "";
            var platform_array = result._0
            if (platform_array){
                platform_html +='<option value=0 >-- select a platform --</option>';
                var arrayLength = platform_array.length;
                for (var i = 0; i < arrayLength; i++) {
                    platform_html += '<option value=' + i +'>' + platform_array[i] + "</option>"
                }
                platform_html += '</select></br>';
            }
            Lighthouse_select_pl.innerHTML = platform_html;
            Lighthouse_Main.style.display = '';
            },
            function (xhr, ajaxOptions, thrownError) {
                LOG("ERROR!");
                LOG(xhr.status)
                LOG(xhr.responseText)
                LOG(thrownError)
                displayResultsErr(xhr.responseText);
                return [];
        });


    $("#Lighthouse_select_pl").change(function() {
        var platf = $(this).find('option:selected').text();
        LOG("Platform selection is " + platf);
        right_window.Lighthouse_select_tech.style.display = 'none';
        right_window.Lighthouse_Loading.style.display = '';
        BJB_CS1_HELPER.runBdbTask(
            "lighthouse_v3_backend",
            {
                'action': 'get_technology_list',
                'platform' : platf
            },
            function (result) {
                LOG("AJAX call was successful. Technology list received");
                LOG(JSON.stringify(result));
                var tech_html = "";
                var tech_array = result._0
                if (tech_array){
                    tech_html +='<option value=0 >-- select a technology --</option>';
                    var arrayLength = tech_array.length;
                    for (var i = 0; i < arrayLength; i++) {
                        tech_html += '<option value=' + i +'>' + tech_array[i] + "</option>"
                    }
                tech_html += '</select></br>';
                }
            Lighthouse_select_tech.innerHTML = tech_html;
            right_window.Lighthouse_select_tech.style.display = '';
            right_window.Lighthouse_Loading.style.display = 'none';
            },
            function (xhr, ajaxOptions, thrownError) {
                LOG("ERROR!");
                LOG(xhr.status)
                LOG(xhr.responseText)
                LOG(thrownError)
                displayResultsErr(xhr.responseText);
                right_window.Lighthouse_Loading.style.display = 'none';
                return [];
          });
    });

    $("#Lighthouse_select_tech").change(function() {
        var platf = $("#Lighthouse_select_pl").find('option:selected').text();
        var tech = $("#Lighthouse_select_tech").find('option:selected').text();
        LOG("Platform and technology selection is :" + platf + " + " + tech);
        right_window.Lighthouse_Loading.style.display = '';
        BJB_CS1_HELPER.runBdbTask(
            "lighthouse_v3_backend",
            {
                'action' : 'get_technology_formatted',
                'platform': platf,
                'technology': tech,
            },
            function (result) {
            right_window.Lighthouse_Loading.style.display = 'none';
            LOG("AJAX call was successful. Technology in HTML format received");
            var guidance = result._0;
            if (guidance){
                displayResults(guidance);
                }
            },
            function (xhr, ajaxOptions, thrownError) {
                LOG("ERROR!");
                LOG(xhr.status)
                LOG(xhr.responseText)
                LOG(thrownError)
                displayResultsErr(xhr.responseText);
                right_window.Lighthouse_Loading.style.display = 'none';
                return [];
            });
    });

};

document.arrive("#TLGPage", {onceOnly: true, existing: true}, function() {
 cs1_Lighthouse_v3();
});

})(BJB_$, BJB_CS1_HELPER);
