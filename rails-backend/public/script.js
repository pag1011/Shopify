async function ask() {
  const question = document.getElementById("question").value;

  const res = await fetch("/api/v1/questions", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      question: question,
      store_id: "demo-store"
    })
  });

  const data = await res.json();

  if (data.error) {
    document.getElementById("response").innerHTML = `
      <p style="color:red">Error: ${data.error}</p>
    `;
    return;
  }

  document.getElementById("response").innerHTML = `
    <h3>Answer</h3>
    <p>${data.answer}</p>

    <h4>Confidence</h4>
    <p>${data.confidence}</p>
  `;
}
