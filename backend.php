<?php
header("Content-Type: application/json");

if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    echo json_encode(["error" => "Invalid request method."]);
    exit;
}

// Sanitize inputs
function get_input($key) {
    return escapeshellarg($_POST[$key] ?? '');
}

$year = get_input("year");
$km_driven = get_input("km_driven");
$mileage = get_input("mileage");
$engine = get_input("engine");
$max_power = get_input("max_power");
$seats = get_input("seats");
$owner = get_input("owner");
$name = get_input("name");
$fuel = get_input("fuel");
$seller_type = get_input("seller_type");
$transmission = get_input("transmission");

// Use correct Python path
$python_path = "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3";
$script_path = "predict.py";

// Run the command
$command = "$python_path $script_path $year $km_driven $mileage $engine $max_power $seats $owner $name $fuel $seller_type $transmission 2>&1";
$output = shell_exec($command);

// Handle result
if ($output === null || trim($output) === "") {
    echo json_encode(["error" => "Prediction failed (no output from script)."]);
} else if (is_numeric(trim($output))) {
    echo json_encode(["predicted_price" => trim($output)]);
} else {
    echo json_encode(["error" => "Python Error Output", "details" => $output]);
}
?>
