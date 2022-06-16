function showIcons(playId, imageGlassId, nameGlassId, descId) {
    document.getElementById(playId).style.display = "block";
    document.getElementById(imageGlassId).style.display = "inline-block";
    document.getElementById(nameGlassId).style.display = "none";
    document.getElementById(descId).style.display = "block";
}

function hideIcons(playId, imageGlassId, nameGlassId, descId) {
    document.getElementById(playId).style.display = "none";
    document.getElementById(imageGlassId).style.display = "none";
    document.getElementById(nameGlassId).style.display = "inline-block";
    document.getElementById(descId).style.display = "none";
}

function play(file) {
    var playerSrc = document.getElementById("playerSrc");
    var player = document.getElementById("player");

    playerSrc.src = file;
    player.load();
    player.play();
}

function btnEditClicked(editBtnId) {
    const all_buttons = document.getElementsByClassName("btn-edit-band");
    for (const i of Array(all_buttons.length).keys()) {
        var button = document.getElementById(all_buttons[i].id);
        button.style.setProperty("background-color", "var(--background-color)");
        button.style.setProperty("color", "var(--primary-color)");
        button.innerText = 'edytuj >>';
    }

    var button = document.getElementById(editBtnId);
    button.style.setProperty("background-color", "var(--primary-color)");
    button.style.setProperty("color", "var(--background-color)");
}

function hideAllForms() {
    const all_forms = document.getElementsByClassName("edit-form");
    for (const i of Array(all_forms.length).keys()) {
        var form = document.getElementById(all_forms[i].id);
        form.style.display = "none";
    }
}

function changeEditBtnName(choiceBtnId, editBtnId, dropdownId) {
    var buttonChoice = document.getElementById(choiceBtnId);
    var buttonEdit = document.getElementById(editBtnId);
    const textOfChoice = buttonChoice.innerText;

    btnEditClicked(editBtnId);
    buttonEdit.innerText = textOfChoice;
}

function editBandAction(choiceBtnId, editBtnId, dropdownId, formId) {
    hideAllForms();
    changeEditBtnName(choiceBtnId, editBtnId, dropdownId);
    document.getElementById(formId).style.display = 'block';
}

function editSongsAction(choiceBtnId, editBtnId, dropdownId, formId) {
    hideAllForms();
    changeEditBtnName(choiceBtnId, editBtnId, dropdownId);
    document.getElementById(formId).style.display = 'block';

    const deleteForms = document.getElementsByClassName("songDeleteFormClass");

    for (const i of Array(deleteForms.length).keys()) {
        if (deleteForms[i].id == "songDeleteFormId-0") {
            deleteForms[i].style.display = "none";
        }
    }
}

function editPrivilegesAction(choiceBtnId, editBtnId, dropdownId, formId) {
    hideAllForms();
    changeEditBtnName(choiceBtnId, editBtnId, dropdownId);
    document.getElementById(formId).style.display = 'block';
}

function editLinksAction(choiceBtnId, editBtnId, dropdownId, formId) {
    hideAllForms();
    changeEditBtnName(choiceBtnId, editBtnId, dropdownId);
    document.getElementById(formId).style.display = 'block';
}

function newBandAction(newBandForm) {
    hideAllForms()

    const all_buttons = document.getElementsByClassName("btn-edit-band");
    for (const i of Array(all_buttons.length).keys()) {
        var button = document.getElementById(all_buttons[i].id);
        button.style.setProperty("background-color", "var(--background-color)");
        button.style.setProperty("color", "var(--primary-color)");
        button.innerText = 'edytuj >>';
    }

    document.getElementById("new-band-form").style.display = "block";
}