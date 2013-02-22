$(document).ready(function(){
    $.getJSON('get_achievements', function(achievements){
        $.getJSON('get_unlocked_achievements', function(unlocked_achievements){
            display_no_achievements_message_if_condition_apply(achievements);
            populate_badge_list(achievements, unlocked_achievements);           
        });        
    }); 

    function display_no_achievements_message_if_condition_apply(achievements)
    {
        if(achievements.length === 0)
        {
            $("#badges ul").hide();
            $("#badges").append(
                '<p style="text-align:center;">There are currently no achievements to unlock' +
                ' - but fear not, some will be added in the near future.<br/><br/></p>'
            );
        }
    }

    function populate_badge_list(achievements, unlocked_achievements)
    {
        var id_count = 0;

        $.each(achievements, function(index) {
            var achievement = achievements[index];
            unlocked_ach_index = get_index_of_value_in_2D_array(achievement, unlocked_achievements);

            if(unlocked_ach_index != -1)
            {
                append_badge_information(
                    id_count++, 
                    achievement.image_url, 
                    achievement.title, 
                    achievement.description, 
                    unlocked_achievements[unlocked_ach_index].unlocked_date
                );
            }
            else
            {
                append_badge_information(
                    id_count++, 
                    '../img/achievements/locked_achievement.jpeg', 
                    achievement.title, 
                    achievement.description, 
                    ''
                );
            }   
        });
    }

    function get_index_of_value_in_2D_array(value, array)
    {
        var index = -1;
        var i = 0;

        while(i < array.length && index == -1)
        {
            if(value.title == array[i].achievement.title)
                index = i;
            i++;
        }

        return index;
    }

    function append_badge_information(id_count, image_url, title, description, date)
    {
        append_badge_information_to_list(id_count, image_url, title, date);
        append_badge_information_to_modal(id_count, image_url, title, description, date);
    }

    function append_badge_information_to_list(id_count, image_url, title, date)
    {    
        $("#badges ul").append(            
            '<li class="span2">' +
                '<div id="' + id_count + '" class="thumbnail" style="width:130px; height:180px;">' +
                    '<a href="#' + id_count + '">' +
                        '<img src="' + image_url + '"/>' +
                    '</a>' +
                    '<a href="#' + id_count + '">' +
                        '<p id="title" style="text-align:center;">' + title + '</p>' +
                    '</a>' +
                    '<p id="date" style="text-align:center;">' + date + '</p>' +
                '</div>' +
            '</li>'
        );
    }

    function append_badge_information_to_modal(id_count, image_url, title, description, date)
    {     
        $("#" + id_count).click(function(modal_object)
        {
            $("#view_achievement_modal").modal('show');
            $("#modal_body_div").html(
                '<div id="image_inner_div" style="float: left; width: 40%;">' +
                    '<img src="' + image_url + '" height="200" width="200" border="0"/>' +
                '</div>' + 
                '<div id="details_inner_div" style="float: right; width: 60%;">' + 
                    '<h3 id="title" style="text-align:center;">' + title + '</h3>' +
                    '<p id="title" style="text-align:center;">' + description + '</p>' +
                '</div>'
            );

            if(date !== "")
            {
                $("#details_inner_div").append(
                    '<p id="date" style="text-align:center;">Badge unlocked at: ' + date + '</p>'
                );
            }
        });        
    }

    $('#closeButton_view').click(function() { 
        $('#view_achievement_modal').modal('hide'); 
    });
});



