var tagFieldsList = new Array();
var minTagsNumber = 1;
var divName = "tag_list_div";

function initTags() {
    for(var i = 0; i < minTagsNumber; ++i) {
        add();
    }
}

function add() {

    var element = document.createElement("input");
    var close = document.createElement("Label")
    var div = document.getElementById(divName);
 

    element.setAttribute("type", "text");
    element.setAttribute("value", "");
    element.setAttribute("name", "tag_list");
    element.setAttribute("style", "width:200px");
    element.setAttribute("onkeyup", "tagTypedHandler(this)");


    close.innerHTML = "&nbsp;x<br>";
    close.setAttribute("onclick", "removeTag(this)");

    div.appendChild(element);
    div.appendChild(close);

    tagFieldsList.push([element, close]);
}

function removeTag(closeElement) {
    var ind = 0;
    for(var i = 0; i < tagFieldsList.length; ++i) {
        if(tagFieldsList[i][1] == closeElement) break;
        ind++;
    }
    if(ind < tagFieldsList.length - 1) {
        tagFieldsList[ind][0].remove();
        tagFieldsList[ind][1].remove();
        tagFieldsList.splice(ind, 1);
    }
}

function emptyTagHandler(textField) {
    var ind = 0;
    for(var i = 0; i < tagFieldsList.length; ++i) {
        if(tagFieldsList[i][0] == textField) break;
        ind++;
    }
    if(ind < tagFieldsList.length - 1) {
        tagFieldsList[ind][0].remove();
        tagFieldsList[ind][1].remove();
        tagFieldsList.splice(ind, 1);
    }
}

function tagTypedHandler(textField) {
    if(textField.value.length > 0) {
        var ind = 0;
        for(var i = 0; i < tagFieldsList.length; ++i) {
            if(tagFieldsList[i][0] == textField) break;
            ind++;
        }
        if(ind == tagFieldsList.length - 1) add();
    }
    else emptyTagHandler(textField);
}
