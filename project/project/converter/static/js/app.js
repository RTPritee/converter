document.getElementById("upload-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const fileInput = document.getElementById("file");
    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    const response = await fetch("/convert/", {
        method: "POST",
        body: formData,
    });

    if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.style.display = "none";
        a.href = url;
        a.download = "output.csv";
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
    } else {
        alert("Error converting file.");
    }
});
