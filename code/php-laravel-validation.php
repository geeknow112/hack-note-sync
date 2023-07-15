// ```php
$rules = [
    'email' => 'required|email',
];
// ```


// ```php
use Illuminate\Support\Facades\Validator;

$data = [
    'email' => $request->input('email'),
];

$validator = Validator::make($data, $rules);

if ($validator->fails()) {
    // バリデーションエラーが発生した場合の処理
}
// ```


// ```php
return view('form')->withErrors($validator);
// ```


// ```php
@if ($errors->has('email'))
    <span class="invalid-feedback" role="alert">
        <strong>{{ $errors->first('email') }}</strong>
    </span>
@endif
// ```
