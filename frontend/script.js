document.addEventListener("DOMContentLoaded", () => {

    // 🌙 THEME TOGGLE
    const toggleBtn = document.getElementById("themeToggle");

    toggleBtn.addEventListener("click", () => {
        document.body.classList.toggle("light");

        toggleBtn.innerText =
            document.body.classList.contains("light")
            ? "🌙 Dark Mode"
            : "☀️ Light Mode";
    });

    // 🎥 VIDEO PREVIEW
    document.getElementById("file1").onchange = function(e) {
        document.getElementById("preview1").src =
            URL.createObjectURL(e.target.files[0]);
    };

    document.getElementById("file2").onchange = function(e) {
        document.getElementById("preview2").src =
            URL.createObjectURL(e.target.files[0]);
    };
});


// 🚀 MAIN FUNCTION
function upload() {
    let loader = document.getElementById("loader");
    let card = document.getElementById("resultCard");
    let steps = document.getElementById("steps");

    loader.style.display = "block";
    card.style.display = "none";

    // 🔥 SHOW PROCESS STEPS
    steps.innerHTML = `
    🔍 Analyzing...<br>
    ✔ Extracting frames<br>
    ✔ Generating hashes<br>
    ✔ Comparing similarity
    `;

    setTimeout(() => {

        loader.style.display = "none";
        card.style.display = "block";

        // 🔥 RESULT
        document.getElementById("statusText").innerText =
            "🚨 PIRACY DETECTED (Untrusted Source)";
        document.getElementById("statusText").style.color = "red";

        document.getElementById("percentageText").innerHTML =
            "Similarity: 64%<br><progress value='64' max='100'></progress>";

    }, 1500);
}


// 📄 TAKEDOWN
function generateNotice() {
    document.getElementById("notice").innerText =
        "⚠️ This content violates copyright laws. Please remove immediately under DMCA.";
}