// TODO: Convert to class

CNDCE.loadCheckins = new Promise((resolve)=>{
    $(function(){
        const $checkinTable = $('.cndce-checkin-table');
        const $filterDateRange = $('.filter-date-range input');

        // Init DateRange picker
        $filterDateRange.daterangepicker({
            timePicker: true
        }, __onDateRangeChange)

        
        // Load data
        $.ajax({
            url: '/api/checkin/table',
            success: function(json){
    
                CNDCE.checkinData = json;
                CNDCE.checkinDataVisible = json.checkins;
    
                $checkinTable.bootstrapTable({
                    data: json.checkins
                });

                CNDCE.__initGroupedByPresets();

                resolve(json);
            },
            error: function(e){
                console.error(e);
                alert('There was an error in retrieving the data. Check in console for more details or reload the page');
            }
        })


        function __onDateRangeChange(start, end, label){
            const data = CNDCE.checkinData.checkins

            const dateStart = new Date(start._d);
            const dateEnd = new Date(end._d);


            CNDCE.updateCheckinData(data.filter((d, i)=>{
                const date = new Date(d.date);

                return isDateValid = date >= dateStart && date <= dateEnd;
            }))

        }

        // Events
        $('#cndce-reset-button').click(function(){
            CNDCE.updateCheckinData(CNDCE.checkinData.checkins)
        })
    
    })
});


CNDCE.updateCheckinData = (newData) => {
    const $checkinTable = $('.cndce-checkin-table');

    CNDCE.checkinDataVisible = newData;

    CNDCE.checkinData.checkins.forEach((d, i)=>{
        if(CNDCE.checkinDataVisible.indexOf(d) != -1){
            $checkinTable.bootstrapTable('showRow', {index: i})

        }else{
            $checkinTable.bootstrapTable('hideRow', {index: i})

        }
    })


    // Update grouped by presets
    CNDCE.__initGroupedByPresets();

    if(CNDCE.cndcePie){
        CNDCE.cndcePie.updateD3();
        console.log('Updated pie')
    }
}


CNDCE.groupby = (array, getGroupByKey, getAggregate)=>{
    return array.reduce((group, item)=>{
        key = getGroupByKey(item);
        groupItem = group[key];

        return {
            ...group,
            [key]: {
                ...groupItem ? {
                    ...groupItem,
                    ...getAggregate(groupItem, item)
                } : item
            }
        }
    }, {})
}


CNDCE.__initGroupedByPresets = () => {
    CNDCE.groupedBy = {
        // Group by tag
        tag: CNDCE.groupby(
            CNDCE.checkinDataVisible, 
            (d)=>d.tag.name, 
            (g, d) => ({
                hours: g.hours + d.hours,
                activity: [
                    ...Array.isArray(g.activity) ? g.activity : [g.activity],
                    d.activity
                ],
                date: [
                    ...Array.isArray(g.date) ? g.date : [g.date],
                    d.date
                ]
            }) 
        )
    }
}



CNDCE.loader.addLoadQueue(CNDCE.loadCheckins)
