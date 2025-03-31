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
  fetch("https://5ab2-110-226-183-128.ngrok-free.app/docs") 
  // Backend ka API URL
  .then(response => response.json())  
  .then(data => {
      const tableBody = document.getElementById("masters-table");
      tableBody.innerHTML = ""; 
      
      data.data.forEach(row => {
          let tr = document.createElement("tr");
          tr.innerHTML = `
              <td>${row.id}</td>
              <td>${row.name}</td>
              <td>${row.category}</td>
              <td>${row.status}</td>
          `;
          tableBody.appendChild(tr);
      });
  })
  .catch(error => console.error("Error fetching data:", error));
}
