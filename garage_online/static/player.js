var playerSrc = document.getElementById("playerSrc");
var player = document.getElementById("player");

function play(file) {
    playerSrc.src = file;
    player.load();
    player.play();
}