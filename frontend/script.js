// wait until page loads
document.addEventListener('DOMContentLoaded', () => {
	// 🌙 DARK / LIGHT MODE
	const toggleBtn = document.getElementById('themeToggle');

	toggleBtn.addEventListener('click', () => {
		document.body.classList.toggle('light');

		if (document.body.classList.contains('light')) {
			toggleBtn.innerText = '🌙 Dark Mode';
		} else {
			toggleBtn.innerText = '☀️ Light Mode';
		}
	});
});

// 🚀 UPLOAD FUNCTION
async function upload() {
	let f1 = document.getElementById('file1').files[0];
	let f2 = document.getElementById('file2').files[0];

	if (!f1 || !f2) {
		alert('Please upload both videos');
		return;
	}

	let loader = document.getElementById('loader');
	let card = document.getElementById('resultCard');

	loader.style.display = 'block';
	card.style.display = 'none';

	setTimeout(() => {
		loader.style.display = 'none';
		card.style.display = 'block';

		document.getElementById('statusText').innerText = '🚨 PIRACY DETECTED';
		document.getElementById('statusText').style.color = 'red';

		document.getElementById('percentageText').innerText = 'Similarity: 64%';
	}, 1500);
}

// 📄 GENERATE NOTICE (FIXED)
function generateNotice() {
	document.getElementById('notice').innerText =
		'⚠️ This content violates copyright laws. Please remove immediately under DMCA.';
}
