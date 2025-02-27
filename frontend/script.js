document.getElementById("quoteButton").addEventListener("click", function() {
    fetch("http://127.0.0.1:5000/quote")
    .then(response => response.json())  // Convert response to JSON
    .then(data => {
        document.getElementById("quoteDisplay").innerText = `"${data.quote}" - ${data.driver}`;
    })
    .catch(error => console.error("Error fetching quote:", error));
});

