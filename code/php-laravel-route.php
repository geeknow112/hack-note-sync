// ```php
Route::get('/hello', 'HelloController@index');
// ```


// ```php
Route::post('/hello', 'HelloController@store');
// ```


// ```php
Route::put('/hello/{id}', 'HelloController@update');
Route::patch('/hello/{id}', 'HelloController@update');
Route::delete('/hello/{id}', 'HelloController@destroy');
// ```


// ```php
Route::get('/users/{id}', function ($id) {
    return 'User '.$id;
});
// ```


// ```php
Route::get('/users/{user}', function (App\Models\User $user) {
    return $user;
});
// ```
