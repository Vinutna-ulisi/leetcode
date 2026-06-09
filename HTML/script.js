let hour = document.getElementById("hours");
let minute = document.getElementById("minutes");
let second = document.getElementById("seconds");
let sec = 0;
let min = 0;    
let hr = 0;
let timer = null;

function startTimer() {
    timer =setInterval(() => {
    sec++;
    second.innerHTML = sec < 10 ? "0" + sec : sec;
    if (sec > 59) {
        sec = 0;
        second.innerHTML = "00";
        min++;
        minute.innerHTML = min < 10 ? "0" + min : min;
    }
    if (min > 59) {
        min = 0;
        minute.innerHTML = "00";
        hr++;
        hour.innerHTML = hr < 10 ? "0" + hr : hr;
    }
    if (hr > 59) {
        hour.innerHTML = "00";
    }   
    console.log(sec, min, hr);
}, 1000);
}

function stopTimer() {
    clearInterval(timer);
}

function resetTimer() {
    clearInterval(timer);
    sec = 0;
    min = 0;
    hr = 0;
    second.innerHTML = "00";
    minute.innerHTML = "00";
    hour.innerHTML = "00";
}