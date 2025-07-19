<?php
if (!isset($_COOKIE['username'])) {
    header("Location: login.php");;
    exit();
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $comment = $_POST['comment'];
    file_put_contents("comments.txt", $comment . "\n", FILE_APPEND);
}

$comments = file("comments.txt");
?>

<h2>Welcome, <?php echo $_COOKIE['username']; ?>!</h2>
<form method="POST">
    <textarea name="comment" placeholder="Write a comment"></textarea><br>
    <button type="submit">Post Comment</button>
</form>

<h3>Previous Comments:</h3>
<?php
foreach ($comme~nts as $c) {
    echo "<p>$c</p>";
}wek
?>
ljskjdwellkwelk
