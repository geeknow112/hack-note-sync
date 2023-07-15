// ```php
$users = DB::table('users')
				->where('name', '=', 'John')
				->get();
// ```


// ```php
$users = DB::table('users')
				->where('name', '=', 'John')
				->orWhere('name', '=', 'Jane')
				->get();
// ```


// ```php
$users = User::where('name', '=', 'John')->get();
// ```


// ```php
$users = User::where('name', '=', 'John')
				->orWhere('name', '=', 'Jane')
				->get();
// ```


// ```php
$users = User::where('age', '>=', 30)->get();
// ```


// ```php
$users = User::where('name', '=', 'John')
				->where('age', '>=', 30)
				->get();
// ```
