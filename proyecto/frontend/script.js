document.getElementById("form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const nombre = document.getElementById("nombre").value;
    const email = document.getElementById("email").value;

    await fetch("http://localhost:5000/personas", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nombre, email }),
    });

    loadPersonas();
});

async function loadPersonas() {
    const res = await fetch("http://localhost:5000/personas");
    const personas = await res.json();
    const ul = document.getElementById("personas");
    ul.innerHTML = "";
    personas.forEach(([id, nombre, email]) => {
        const li = document.createElement("li");
        li.textContent = `${nombre} (${email})`;
        ul.appendChild(li);
    });
}

loadPersonas();
