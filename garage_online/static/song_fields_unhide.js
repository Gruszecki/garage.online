window.onload = function lyrics_toggle() {
    if (this.checked) {
    console.log('this.checked True')
        document.getElementById("language").style.display = 'block';
        document.getElementById("lyrics").style.display = 'block';
    } else {
    console.log('this.checked False')
        document.getElementById("language").style.display = 'none';
        document.getElementById("lyrics").style.display = 'none';
    }
}
console.log("Jestem w JavaScript. Wchodze do funkcji.")
document.getElementById("has_lyrics").onclick = lyrics_toggle;