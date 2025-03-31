// script.js
function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  sidebar.style.display = sidebar.style.display === "block" ? "none" : "block";
}

function uploadFile() {
  alert("File uploaded successfully!");
}

document.addEventListener("DOMContentLoaded", function () {
  fetchMastersData();
});

// Masters data fetch karne ka function
function fetchMastersData() {
  fetch("http://127.0.0.1:8000/read_master_input/")
    .then(response => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then(data => {
      const tableBody = document.getElementById("masters-table");
      tableBody.innerHTML = "";  // Clear existing data

      data.forEach(row => {
        let tr = document.createElement("tr");
        tr.innerHTML = `
          <td>${row.id || "N/A"}</td>
          <td>${row.name || "N/A"}</td>
          <td>${row.category || "N/A"}</td>
          <td>${row.sub_category || "N/A"}</td>
        `;
        tableBody.appendChild(tr);
      });
    })
    .catch(error => console.error("Error fetching data:", error));
}
