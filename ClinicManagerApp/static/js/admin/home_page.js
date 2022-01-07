var gChart = null;
var gBgChart = null;

function getCustomerArriveFrequently() {
  fetch("/api/homepage/customer_arrive_frequenly")
    .then(function (res) {
      return res.json();
    })
    .then(function (datas) {
      $("#month").text(datas["month"]);
      $("#year").text(datas["year"]);
      labels = datas["days"];
      data = datas["datas"];
      createChart(
        (id = "customer_arrive_frequently_chart"),
        (type = "bar"),
        (label = `Tần suất khách hàng đến trong tháng ${datas["month"]} / ${datas["year"]}`),
        (data = data),
        (labels = labels)
      );
    });
}

function getTopMedicine() {
  fetch("/api/homepage/top_medicine")
    .then(function (res) {
      return res.json();
    })
    .then(function (datas) {
      labels = [];
      data = [];
      for (let i = 0; i < datas.length; i++) {
        labels.push(datas[i]["name"]);
        data.push(
          datas[i]["total_price"]
          .substring(0, datas[i]["total_price"].indexOf(" "))
          .replaceAll(",", "")
        );
      }
      createChart(
        (id = "top_medicine_chart"),
        (type = "line"),
        (label = "Các loại thuốc bán chạy nhất"),
        (data = data),
        (labels = labels)
      );
    });
}

function getRevenue() {
  fetch("/api/homepage/revenue")
    .then(function (res) {
      return res.json();
    })
    .then(function (datas) {
      $("#today_revenue").text(datas["today"]);
      $("#yesterday_revenue").text(datas["yesterday"]);
      labels = ["Doanh thu hôm qua", "Doanh thu hôm nay"];
      data = [];
      data.push(
        datas["today"]
        .substring(0, datas["today"].indexOf(" "))
        .replaceAll(",", "")
      );
      data.push(
        datas["yesterday"]
        .substring(0, datas["yesterday"].indexOf(" "))
        .replaceAll(",", "")
      );
      createChart(
        (id = "total_income_chart"),
        (type = "pie"),
        (label = "Doanh thu"),
        (data = data),
        (labels = labels)
      );
    });
}

function getGeneralAmount() {
  fetch("/api/homepage/general_amount")
    .then(function (res) {
      return res.json();
    })
    .then(function (datas) {
      $("#department_amount").text(datas["department_amount"]);
      $("#staff_amount").text(datas["staff_amount"]);
      $("#customer_amount").text(datas["customer_amount"]);
      $("#medicine_amount").text(datas["medicine_amount"]);
      $("#category_amount").text(datas["category_amount"]);
    });
}

//create chart
function createChart(id = "", type = "", label = "", data = [], labels = []) {
  var backgroundColor = [];
  var borderColor = [];
  for (let i = 0; i < data.length; i++) {
    r = Math.floor(Math.random() * 255 + 1);
    g = Math.floor(Math.random() * 255 + 1);
    b = Math.floor(Math.random() * 255 + 1);
    backgroundColor.push(`rgba(${r},${g}, ${b}, 0.7)`);
    borderColor.push(`rgba(${r},${g}, ${b}, 1)`);
  }
  const ctx = document.getElementById(id).getContext("2d");

  const bgColorPDF = {
    id: "bgColorPDF",
    beforeDraw: (chart) => {
      const {
        ctx,
        width,
        height
      } = chart;
      ctx.fillStyle = gBgChart;
      ctx.fillRect(0, 0, width, height);
      ctx.restore();
    },
  };
  new Chart(ctx, {
    type: type,
    data: {
      labels: labels,
      datasets: [{
        label: label,
        data: data,
        backgroundColor: backgroundColor,
        borderColor: borderColor,
        borderWidth: 1,
      }, ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
    plugins: [bgColorPDF],
  });
}

$(document).ready(function () {
  gBgChart = $(".card").css("background-color");

  // check theme color when user refesh page
  window.onload = function () {
    if ($("body").attr('data-background-color') == 'bg1')
      gBgChart = '#ffffff';
    else if ($("body").attr('data-background-color') == 'bg2')
      gBgChart = '#ffffff';
    else if ($("body").attr('data-background-color') == 'bg3')
      gBgChart = '#ffffff';
    else
      gBgChart = '#202940';
    getGeneralAmount();
    getRevenue();
    getCustomerArriveFrequently();
    getTopMedicine();
  };
  // check theme color when user click change bg
  $(".changeBackgroundColor").click(function () {
    if ($("body").attr("data-background-color") == "bg1") gBgChart = "#ffffff";
    else if ($("body").attr("data-background-color") == "bg2")
      gBgChart = "#ffffff";
    else if ($("body").attr("data-background-color") == "bg3")
      gBgChart = "#ffffff";
    else gBgChart = "#202940";
    getRevenue();
    getCustomerArriveFrequently();
    getTopMedicine();
  });
});