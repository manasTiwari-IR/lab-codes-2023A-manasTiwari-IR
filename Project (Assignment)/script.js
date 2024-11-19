document.addEventListener("DOMContentLoaded", () => {
  const getNewsButton = document.querySelector("#get_news");
  const newsContainer = document.getElementById("news-container");
  getNewsButton.addEventListener("click", async () => {
    const category = document.getElementById("category").value;
    //console.log(category);
    getNewsButton.disabled = true;
    document.getElementById("category").disabled = true;
    
    let Topic = category[0].toUpperCase() + category.slice(1);
    document.querySelector(".topic").innerHTML = Topic;
    newsContainer.innerHTML = "<p>Loading...</p>";

    try {
      const response = await axios.post("http://127.0.0.1:5001/scrape", {
        user: `${category}`, // Adjust the user parameter as needed
      });

      const data = response.data;
      console.log(data);

      if (response.status === 200) {
        newsContainer.innerHTML = ""; // Clear previous results
        data["data"].forEach((item) => {
          const newsItem = document.createElement("div");
          newsItem.classList.add("news-item");
          newsItem.innerHTML = `
          <img src="${item["Image URL"]}" alt="News Image" />
                        <h2>${item["Headline"]}</h2>
                        <p>${item["Paragraph"]}</p>
                    `;
          newsContainer.appendChild(newsItem);
        });
      } else {
        console.log("Error fetching data:", data.error);
        newsContainer.innerHTML = `<p>Error: ${data.error}</p>`;
      }
    } catch (error) {
      newsContainer.innerHTML = `<p>Failed to fetch news: ${error.message}</p>`;
    } finally {
      getNewsButton.disabled = false;
      document.getElementById("category").disabled = false;
    }
  });
});
