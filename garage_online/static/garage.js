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

function btnEditClicked(btn) {
    const all_buttons = document.getElementsByClassName("btn-edit-band");

    for (const i of Array(all_buttons.length).keys()) {
        var button = document.getElementById(all_buttons[i].id)
        button.style.setProperty("background-color", "var(--background-color)")
        button.style.setProperty("color", "var(--primary-color)")
    }

    var button = document.getElementById(btn);
    button.style.setProperty("background-color", "var(--primary-color)");
    button.style.setProperty("color", "var(--background-color)");
}

function changeEditBtnName(bandId, btnId, editBtnId) {
    var buttonChoice = document.getElementById(btnId);
    var buttonEdit = document.getElementById(editBtnId);
    const textOfChoice = buttonChoice.innerText;

    buttonEdit.innerText = textOfChoice;
    btnEditClicked(editBtnId);
}

