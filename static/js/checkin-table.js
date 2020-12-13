CNDCE.loadCheckins = new Promise((resolve)=>{
    $(function(){
        const $checkinTable = $('.cndce-checkin-table');
    
    
        $.ajax({
            url: '/api/checkin/table',
            success: function(json){
    
                CNDCE.checkinData = json;
    
                $checkinTable.bootstrapTable({
                    data: json.checkins
                });

                // Group by tag
                CNDCE.groupedBy = {
                    tag: CNDCE.groupby(
                        json.checkins, 
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

                resolve(json);
            },
            error: function(e){
                console.error(e);
                alert('There was an error in retrieving the data. Check in console for more details or reload the page');
            }
        })
    
    })
});


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



CNDCE.loader.addLoadQueue(CNDCE.loadCheckins)
