<?php
// 获取输入的内容
$request = file_get_contents("php://input");

// 按json格式解析成一个 php对象
$json_obj = json_decode($request);

// 按json格式解析成一个 php关联数组
$json_obj_array = json_decode($request, true);

$json_obj_array['version'];
$json_obj_array['name'];
$json_obj_array['structure']['a'];

// 生成结果的json数组
$json_array = array(
	'version' => 'mjson_v1.0',
	'name' => 'http_result',
	'structure' => array(
		'code' => $json_obj_array['structure']['a'],
		'message' => 'Hello Device!'
	)
	);

// 转换成json文本，并把文本发给客户端
echo json_encode($json_array);
?>
