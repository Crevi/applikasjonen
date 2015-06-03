$(document).ready(function(){
	//the on-click function event for the likes button with ajax 
	//so that the page does not reload upon click
	$(".add-comment-link").click(function(event) {
		event.preventDefault();
		var comment_id = $(this).data("commentid");
		$.ajax({
			url: $('#add_likes_url').val() + "/" + comment_id
		}) 
		.done(function(data){
			var comment_updated = data['comment_updated'];
			var likes_element_id = '#id-likes-for-comment-' + comment_id;
			$(likes_element_id).html(comment_updated);
		});
	});

});