function lyrics_toggle() {
    console.log(has_lyrics)
    if (has_lyrics.checked) {
        document.getElementById("id_language").style.display = 'block';
        document.getElementById("id_lyrics").style.display = 'block';
    } else {
        document.getElementById("id_language").style.display = 'none';
        document.getElementById("id_lyrics").style.display = 'none';
    }
}

const has_lyrics = document.getElementById("id_has_lyrics");
has_lyrics.onclick = lyrics_toggle;

