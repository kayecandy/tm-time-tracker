$(function(){
    $('.cndce-checkin-add-modal').submit(function(e){
        console.log('submit');

        e.preventDefault();

        $form = $(this);

        $form.addClass('disabled');

        $.ajax({
            url: '/api/checkin/add',
            type: 'POST',
            data: $form.serialize(),
            success: ()=>{
                alert('Successfully added entry!')

                $('input', $form).val('');
                $form.removeClass('disabled');

                $('#cndce-checkin-add-modal').modal('hide');
            }
        })
    })
})