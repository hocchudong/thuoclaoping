$(window).load(function() {
    $("tr.interface_row").each(function(){
        var id_row = $(this).attr("id");
        var interface = id_row.split('-')[1];
        console.log(id_row);
        (function network() {   
            $.ajax({
                url: '/ajax/network/' + interface,
                success: function(data_info) {
                    console.log(data_info);
                    $('#interface-' + interface + ' td:nth-child(1)').html(data_info["name_interface"]);
                    $('#interface-' + interface + ' td:nth-child(2)').html(data_info["bytes_sent"]);
                    $('#interface-' + interface + ' td:nth-child(3)').html(data_info["bytes_recv"]);
                },
                failure: function(data_info) {
                    console.log('Got an error total parameter');
                }
            }).then(function() {           // on completion, restart
                setTimeout(network, 10000);  // function refers to itself
            });
        })();
    });

    (function ram_info() {
        $.ajax({
            url: '/ajax/disk',
            dataType: 'json',
            success: function (data) {
                // console.log(data['ram_free']);
                var chart = new CanvasJS.Chart("disk_info",
                {
                    title:{
                        text: "Disk / (%)"
                    },
                    legend: {
                        maxWidth: 350,
                        itemWidth: 120,
                        horizontalAlign: "right",
                        verticalAlign: "center"
                    },
                    data: [
                    {
                        type: "pie",
                        showInLegend: true,
                        toolTipContent: "{y}%",
                        legendText: "{indexLabel}: {y}%",
                        dataPoints: [
                            { y: data['disk_used'], indexLabel: "disk used", color: "#778899"},
                            { y: data['disk_free'], indexLabel: "disk free", color: "#E9967A"}
                        ]
                    }
                    ]
                });
                chart.render();
            },
            failure: function (data) {
                alert('Got an error dude');
            }
        }).then(function () {           // on completion, restart
            setTimeout(disk_info, 10000);  // function refers to itself
        });
})();

    (function disk_info() {
        $.ajax({
            url: '/ajax/ram',
            dataType: 'json',
            success: function (data) {
                // console.log(data['disk_free']);
                var chart = new CanvasJS.Chart("ram_info",
                {
                    title:{
                        text: "RAM (%)"
                    },
                    legend: {
                        maxWidth: 350,
                        itemWidth: 120,
                        horizontalAlign: "right",
                        verticalAlign: "center"
                    },
                    data: [
                    {
                        type: "pie",
                        showInLegend: true,
                        toolTipContent: "{y}%",
                        legendText: "{indexLabel}: {y}%",
                        dataPoints: [
                            { y: data['ram_used'], indexLabel: "ram used", color: "#F0E68C"},
                            { y: data['ram_free'], indexLabel: "ram free", color: "#3CB371" }
                        ]
                    }
                    ]
                });
                chart.render();
            },
            failure: function (data) {
                alert('Got an error dude');
            }
        }).then(function () {           // on completion, restart
            setTimeout(ram_info, 10000);  // function refers to itself
        });
})();

    (function cpu_util(){
        $.ajax({
            url: 'ajax/cpu_util',
            success: function(data) {
                $('#cpu_user').html(data['cpu_user']);
                $('#cpu_nice').html(data['cpu_nice']);
                $('#cpu_system').html(data['cpu_system']);
                $('#cpu_iowait').html(data['cpu_iowait']);
                $('#cpu_idle').html(data['cpu_idle']);
                $('#cpu_steal').html(data['cpu_steal']);
                $('#load1m').html(data['load1m']);
                $('#load5m').html(data['load5m']);
                $('#load15m').html(data['load15m']);
            },
            failure: function(data) {
                console.log('Got an error total parameter');
            }
        }).then(function() {           // on completion, restart
            setTimeout(cpu_util, 10000);  // function refers to itself
        });
    })();

    (function http_queries() {
            $.ajax({
                url: '/ajax/http_queries',
                dataType: 'json',
                success: function (data) {
                    // console.log(data);
                    var dps = [];
                    var chart1 = new CanvasJS.Chart("chartContainer1", {
                        exportEnabled: true,
                        title: {
                            text: "HTTP queries"
                        },
                        // legend: {
                        //     horizontalAlign: "left",
                        //     verticalAlign: "center"
                        // },
                        axisY: {
                            includeZero: false,
                            suffix: " ops"
                        },
                        data: [{
                            name: "HTTP queries: {y} ops",
                            type: "spline",
                            markerSize: 0,
                            xValueType: "dateTime",
                            showInLegend: true,
                            dataPoints: dps
                        }]

                    });
                    var xVal = data[0]['time'];
                    var yVal = data[0]['non_negative_derivative'];
                    // console.log(yVal);
                    var dataLength1 = data.length;
                    var updateChart1 = function (count) {
                        count = count || 1;
                        // count is number of times loop runs to generate random dataPoints.
                        for (var j = 0; j < count; j++) {
                            yVal = data[j]['non_negative_derivative'];
                            xVal = data[j]['time'];
                            // console.log(xVal);
                            dps.push({
                                x: xVal,
                                y: yVal
                            });
                        }
                        if (dps.length > dataLength1) {
                            dps.shift();
                        }
                        chart1.render();
                    };
                    updateChart1(dataLength1);
                },
                failure: function (data) {
                    alert('Got an error dude');
                }
            }).then(function () {           // on completion, restart
                setTimeout(http_queries, 10000);  // function refers to itself
            });
        })();

    (function server_errors() {
            $.ajax({
                url: '/ajax/server_errors',
                dataType: 'json',
                success: function (data) {
                    // console.log(data);
                    var dps = [];
                    var chart = new CanvasJS.Chart("chartContainer2", {
                        exportEnabled: true,
                        title: {
                            text: "Server errors"
                        },
                        axisY: {
                            includeZero: false,
                            suffix: " ops"
                        },
                        data: [{
                            name: "Server errors: {y} ops",
                            type: "spline",
                            markerSize: 0,
                            xValueType: "dateTime",
                            showInLegend: true,
                            dataPoints: dps
                        }]

                    });
                    var xVal = data[0]['time'];
                    var yVal = data[0]['non_negative_derivative'];
                    console.log(yVal);
                    var dataLength = data.length;
                    var updateChart = function (count) {
                        count = count || 1;
                        // count is number of times loop runs to generate random dataPoints.
                        for (var j = 0; j < count; j++) {
                            yVal = data[j]['non_negative_derivative'];
                            xVal = data[j]['time'];
                            // console.log(xVal);
                            dps.push({
                                x: xVal,
                                y: yVal
                            });
                        }
                        if (dps.length > dataLength) {
                            dps.shift();
                        }
                        chart.render();
                    };
                    updateChart(dataLength);
                },
                failure: function (data) {
                    alert('Got an error dude');
                }
            }).then(function () {           // on completion, restart
                setTimeout(server_errors, 10000);  // function refers to itself
            });
        })();

    (function client_errors() {
        $.ajax({
            url: '/ajax/client_errors',
            dataType: 'json',
            success: function (data) {
                // console.log(data);
                var dps = [];
                var chart = new CanvasJS.Chart("chartContainer3", {
                    exportEnabled: true,
                    title: {
                        text: "Client errors"
                    },
                    axisY: {
                        includeZero: false,
                        suffix: " ops"
                    },
                    data: [{
                        name: "Client_errors: {y} ops",
                        type: "spline",
                        markerSize: 0,
                        xValueType: "dateTime",
                        showInLegend: true,
                        dataPoints: dps
                    }]

                });
                var xVal = data[0]['time'];
                var yVal = data[0]['non_negative_derivative'];
                console.log(yVal);
                var dataLength = data.length;
                var updateChart = function (count) {
                    count = count || 1;
                    // count is number of times loop runs to generate random dataPoints.
                    for (var j = 0; j < count; j++) {
                        yVal = data[j]['non_negative_derivative'];
                        xVal = data[j]['time'];
                        // console.log(xVal);
                        dps.push({
                            x: xVal,
                            y: yVal
                        });
                    }
                    if (dps.length > dataLength) {
                        dps.shift();
                    }
                    chart.render();
                };
                updateChart(dataLength);
            },
            failure: function (data) {
                alert('Got an error dude');
            }
        }).then(function () {           // on completion, restart
            setTimeout(client_errors, 10000);  // function refers to itself
        });
    })();

    (function info_influx() {
        $.ajax({
            url: 'ajax/info_influx',
            success: function(data_info) {
                $('#total_measuere').html(data_info['total_measuere']);
                $('#total_series').html(data_info['total_series']);
                $('#avg_query').html(data_info['avg_query']);
            },
            failure: function(data_info) {
                console.log('Got an error total parameter');
            }
        }).then(function() {           // on completion, restart
            setTimeout(info_influx, 10000);  // function refers to itself
        });
    })();
});
