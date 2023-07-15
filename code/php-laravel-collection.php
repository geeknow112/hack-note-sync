// ```php
$array = [1, 2, 3, 4, 5];

$collection = collect($array);
// ```


// ```php
$users = [
	['name' => 'Alice', 'age' => 25],
	['name' => 'Bob', 'age' => 30],
	['name' => 'Charlie', 'age' => 20],
	['name' => 'Dave', 'age' => 35],
];
// ```


// ```php
$filtered = collect($users)
	->filter(function ($user) {
		return $user['age'] >= 30;
	});
// ```


// ```php
$users = [
	['name' => 'Alice', 'age' => 25],
	['name' => 'Bob', 'age' => 30],
	['name' => 'Charlie', 'age' => 20],
	['name' => 'Dave', 'age' => 35],
];
// ```


// ```php
$names = collect($users)
	->map(function ($user) {
		return $user['name'];
	});
// ```


// ```php
$users = [
	['name' => 'Alice', 'age' => 25],
	['name' => 'Bob', 'age' => 30],
	['name' => 'Charlie', 'age' => 20],
	['name' => 'Dave', 'age' => 35],
];
// ```


// ```php
$sorted = collect($users)
	->sortBy('age');
// ```
