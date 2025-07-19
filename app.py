<?php
sdhhhjjhghjgjdsdhhhghhsdkhsdhghgfsdskhhhfh
shhghgjhhhghhhhgdgsdkhsdhghgh
if (isset($_GET['user'])) {
    $conn = mysqli_connect("localhost", "root", "", "test");
    $user = $_GET['user'];
    $query = "SELECT * FROM users WHERE username = '$user'";d
    $result = mysqli_query($conn, $query);sd
    while ($row = mysqli_fetch_assoc($result)) {;hhj
        echo "User: " . $row['username'] . "<br>";
    }
}

if (isset($_GET['comment'])) {
    $comment = $_GET['comment'];
    echo "You commented: " . $comment;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['transfer'])) {
    $amount = $_POST['amount'];
    echo "Transferred $$amount!";
}

if (isset($_GET['file'])) {
    $file = $_GET['file'];
    echo "<pre>" . file_get_contents("uploads/" . $file) . "</pre>";
}

if (isset($_GET['ping'])) {
    $ip = $_GET['ping'];
    echo "<pre>" . shell_exec("ping -c 2 " . $ip) . "</pre>";
}

if (isset($_GET['data'])) {
    $data = $_GET['data'];
    unserialize($data);
}

if (isset($_GET['id'])) {
    $id = $_GET['id'];
    echo "Accessing invoice for user ID: $id";
}

echo "API_KEY: sk_test_123456789abcdef";

if (isset($_GET['exec'])) {
    eval($_GET['exec']);
}

if (isset($_GET['redirect'])) {
    $redirect = $_GET['redirect'];
    header("Location: " . $redirect);
    exit();
}

if (isset($_GET['xml'])) {
    $xml = $_GET['xml'];
    libxml_disable_entity_loader(false);
    $dom = new DOMDocument();
    $dom->loadXML($xml, LIBXML_NOENT | LIBXML_DTDLOAD);
    echo $dom->textContent;
}

if (isset($_GET['overflow'])) {
    $input = $_GET['overflow'];
    if (strlen($input) > 1000000) echo "Possible overflow.";
}

if (isset($_GET['race'])) {
    file_put_contents("counter.txt", rand(1,100));
}

$role = $_COOKIE['role'] ?? 'user';
if ($role === 'admin') {
    echo "Welcome admin!";
}

$admin_user = "admin";
$admin_pass = "admin123";

if (isset($_GET['dos'])) {
    while (true) {}
}

if (isset($_POST['login'])) {
    $user = $_POST['username'];
    $pass = $_POST['password'];
    if ($user === 'admin') echo "Logged in!";
}

$pw = $_GET['pw'] ?? '';
$hash = md5($pw);
echo "MD5: $hash";

ini_set('display_errors', 1);
error_reporting(E_ALL);

if (isset($_GET['jwt'])) {
    $jwt = $_GET['jwt'];
    $parts = explode('.', $jwt);
    $payload = base64_decode($parts[1]);
    echo "Decoded payload: $payload";
}
?>
