## ```php
$users = DB::table('users')->get();
## ```


## ```php
DB::table('users')->insert(
    ['name' => 'John Doe', 'email' => 'johndoe@example.com']
);
## ```


## ```php
DB::table('users')
    ->where('id', 1)
    ->update(['votes' => 1]);
## ```


## ```php
DB::table('users')->where('votes', '<', 100)->delete();
## ```


## ```php
php artisan make:model User
## ```


## ```php
$users = App\Models\User::all();
## ```


## ```php
$user = new App\Models\User;
$user->name = 'John Doe';
$user->email = 'johndoe@example.com';
$user->save();
## ```


## ```php
$user = App\Models\User::find(1);
$user->votes = 1;
$user->save();
## ```


## ```php
$user = App\Models\User::find(1);
$user->delete();
## ```


## ```php
class User extends Model
{
    public function posts()
    {
        return $this->hasMany(Post::class);
    }
}
## ```


## ```php
$user = App\Models\User::find(1);
$posts = $user->posts;
## ```


## ```php
class User extends Model
{
    public function scopeAdmin($query)
    {
        return $query->where('admin', true);
    }
}
## ```


## ```php
$admins = App\Models\User::admin()->get();
## ```


## ```php
class User extends Model
{
    public function setNameAttribute($value)
    {
        $this->attributes['name'] = strtoupper($value);
    }
}
## ```


## ```php
$user = new App\Models\User;
$user->name = 'John Doe';
$user->email = 'johndoe@example.com';
$user->save();
## ```
