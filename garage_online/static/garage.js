function play(file) {
    var playerSrc = document.getElementById("playerSrc");
    var player = document.getElementById("player");

    playerSrc.src = file;
    player.load();
    player.play();
}

function showIcons(infoId, playId, imageGlassId, nameGlassId) {
    document.getElementById(infoId).style.display = "block";
    document.getElementById(playId).style.display = "block";
    document.getElementById(imageGlassId).style.display = "inline-block";
    document.getElementById(nameGlassId).style.display = "none";
}

function hideIcons(infoId, playId, imageGlassId, nameGlassId) {
    document.getElementById(infoId).style.display = "none";
    document.getElementById(playId).style.display = "none";
    document.getElementById(imageGlassId).style.display = "none";
    document.getElementById(nameGlassId).style.display = "inline-block";
}