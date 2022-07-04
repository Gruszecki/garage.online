let root = document.documentElement;
var filterButtons = document.getElementsByClassName("filter-button");

for (const i of Array(filterButtons.length).keys()) {
    filterButtons[i].style.setProperty("background-color", "var(--background-color)");
    filterButtons[i].style.setProperty("color", "var(--primary-color)");
    filterButtons[i].style.setProperty("border", "2px solid var(--primary-color)");
}

function showIcons(playId, infoId, imageGlassId, nameGlassId, descId) {
    document.getElementById(playId).style.display = "block";
    document.getElementById(infoId).style.display = "block";
    document.getElementById(imageGlassId).style.display = "inline-block";
    document.getElementById(nameGlassId).style.display = "none";
    document.getElementById(descId).style.display = "block";
}

function hideIcons(playId, infoId, imageGlassId, nameGlassId, descId) {
    document.getElementById(playId).style.display = "none";
    document.getElementById(infoId).style.display = "none";
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

function editSthAction(choiceBtnId, bandId, formId) {
    hideAllForms();
    changeEditBtnName(choiceBtnId, `btn-edit-${bandId}`, `dropdown-edit-content-${bandId}`);
    document.getElementById(formId).style.display = 'block';
}

function editSongsAction(choiceBtnId, bandId, formId) {
    editSthAction(choiceBtnId, bandId, formId)

    const deleteForms = document.getElementsByClassName("songDeleteFormClass");

    for (const i of Array(deleteForms.length).keys()) {
        if (deleteForms[i].id == "songDeleteFormId-0") {
            deleteForms[i].style.display = "none";
        }
    }
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

function hideLyricsFields(bandId, songId) {
    var form = document.getElementById(`song-edit-form-${bandId}-${songId}`);
    var language = document.getElementById(`language-${bandId}-${songId}`);
    var lyrics = document.getElementById(`lyrics-${bandId}-${songId}`);

    if(form.elements["has_lyrics"].checked){
        language.style.display = "block";
        lyrics.style.display = "block";
    } else {
        language.style.display = "none";
        lyrics.style.display = "none";
    }
}

function checkboxButton(checkboxId, buttonId) {
    checkbox = document.getElementById(checkboxId);
    button = document.getElementById(buttonId);

    if(checkbox.checked) {
        button.style.setProperty("background-color", "var(--primary-color)");
        button.style.setProperty("color", "var(--background-color)");
    } else {
        button.style.setProperty("background-color", "var(--background-color)");
        button.style.setProperty("color", "var(--primary-color)");
    }
}

function copySearchInput() {
    mainInput = document.getElementById("search-place");
    canvasInput = document.getElementById("search-place-canvas");

    canvasInput.value = mainInput.value;
}

window.addEventListener("load", startup_color_pickers, false);
function startup_color_pickers() {
    var primary_color = document.getElementById("primary_color_picker");
    var text_color = document.getElementById("text_color_picker");
    var background_color = document.getElementById("background_color_picker");
    var background_medium_color = document.getElementById("background_medium_color_picker");
    var background_light_color = document.getElementById("background_light_color_picker");

    primary_color.addEventListener("input", changeColorSetPrimary, false);
    text_color.addEventListener("input", changeColorSetText, false);
    background_color.addEventListener("input", changeColorSetBackground, false);
    background_medium_color.addEventListener("input", changeColorSetBackgroundMedium, false);
    background_light_color.addEventListener("input", changeColorSetBackgroundLight, false);
}

function changeColorSetPrimary(event) {
    root.style.setProperty('--primary-color', event.target.value);
}

function changeColorSetText(event) {
    root.style.setProperty('--text-color', event.target.value);
}

function changeColorSetBackground(event) {
    root.style.setProperty('--background-color', event.target.value);
}

function changeColorSetBackgroundMedium(event) {
    root.style.setProperty('--background-medium-color', event.target.value);
}

function changeColorSetBackgroundLight(event) {
    root.style.setProperty('--background-light-color', event.target.value);
}