// ```php
'channels' => [
    'daily' => [
        'driver' => 'daily',
        'path' => storage_path('logs/laravel.log'),
        'level' => 'debug',
        'days' => 14,
    ],
],
// ```


// ```php
use Illuminate\Support\Facades\Log;

Log::info('ログを出力します。');
// ```


// ```php
Log::emergency('緊急のログを出力します。');
// ```


// ```php
use Illuminate\Support\Facades\Log;

// ログを出力する
Log::info('ログを出力します。');

// 緊急のログを出力する
Log::emergency('緊急のログを出力します。');
// ```
