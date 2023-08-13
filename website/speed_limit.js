$(document).ready(function() {
    // Function to update the license information based on the speed limit
    function updateLicenseInfo(speedLimit) {
        var aboveLimitContainer = $('#above-limit-container');
        var belowLimitContainer = $('#below-limit-container');
        aboveLimitContainer.empty(); // Clear previous license information
        belowLimitContainer.empty(); // Clear previous license information

        // Read the CSV file using AJAX
        $.ajax({
            url: '../data /filtered_file.csv',
            dataType: 'text',
            success: function(data) {
                var lines = data.split('\n');
                var aboveLimitLicenses = [];
                var belowLimitLicenses = [];

                // Parse the CSV data and filter based on the speed limit
                for (var i = 1; i < lines.length; i++) {
                    var line = lines[i].trim();
                    if (line.length === 0) continue;

                    var columns = line.split(',');
                    var licenseNumber = columns[1].trim();
                    var speed = parseFloat(columns[2].trim());

                    // Filter based on the speed limit
                    var license = { number: licenseNumber, speed: speed };
                    if (speed <= speedLimit) {
                        belowLimitLicenses.push(license);
                    } else {
                        aboveLimitLicenses.push(license);
                    }
                }

                // Sort the licenses based on speed in ascending order
                aboveLimitLicenses.sort(function(a, b) {
                    return a.speed - b.speed;
                });
                belowLimitLicenses.sort(function(a, b) {
                    return a.speed - b.speed;
                });

                // Display the license information above the limit
                aboveLimitLicenses.forEach(function(license, index) {
                    var licenseInfo = $('<div class="license-info">');
                    licenseInfo.text('License: ' + license.number + ', Speed: ' + license.speed + ' km/h');
                    aboveLimitContainer.append(licenseInfo);
                });

                // Display the license information below the limit
                belowLimitLicenses.forEach(function(license, index) {
                    var licenseInfo = $('<div class="license-info">');
                    licenseInfo.text('License: ' + license.number + ', Speed: ' + license.speed + ' km/h');
                    belowLimitContainer.append(licenseInfo);
                });
            }
        });
    }

    // Event listener for the speed limit input box
    $('#speed-limit-input').on('input', function() {
        var speedLimit = parseFloat($(this).val());
        if (!isNaN(speedLimit)) {
            updateLicenseInfo(speedLimit);
        }
    });
});
