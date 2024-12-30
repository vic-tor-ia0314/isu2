document.getElementById('function-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const functionInput = document.getElementById('function-input').value;

    try {
        const response = await fetch('/plot', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ function: functionInput })
        });

        if (!response.ok) {
            const errorData = await response.json();
            alert(`Error: ${errorData.error}`);
            return;
        }

        const data = await response.json();
        document.getElementById('graph-img').src = data.plot;
    } catch (err) {
        console.error('Error:', err);
        alert('Failed to generate graph.');
    }
});
