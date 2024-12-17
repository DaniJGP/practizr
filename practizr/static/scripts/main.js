const rowForm = document.getElementById('row-form');
const tableBody = document.getElementById('table-body');
const pageType = document.body.dataset.page;

let templateToSend = [];

rowForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get new row values
    const duration = document.getElementById('duration').value;
    const area = document.getElementById('area').value;
    const item = document.getElementById('item').value;
    const note = document.getElementById('note').value;

    // Validate relevant fields
    if (!duration) {
        alert('Duration is required!');
        return;
    }
    if (!area) {
        alert('Area is required!');
        return;
    }

    // Store row in an object, add it to template
    const newRowData = { id: Date.now(), duration, area, item, note };
    templateToSend.push(newRowData);
    console.log(templateToSend);

    // Update DOM table using template data
    const upddateTable = (table, template) => {
        // Clear previous table
        table.innerHTML = '';
        // Key order to add to the table
        const columnOrder = ['duration', 'area', 'item', 'note'];

        // Traverse template array and create a row for each element
        templateToSend.forEach((rowData, index) => {
            // Creates new row
            const row = document.createElement('tr');
            row.id = rowData.id;

            // First cell is the order
            const orderingCell = document.createElement('td');
            orderingCell.textContent = index + 1;
            row.appendChild(orderingCell);

            // Next cells are data
            columnOrder.forEach((key) => {
                const cell = document.createElement('td');
                cell.textContent = rowData[key];
                row.appendChild(cell);
            });

            // Delete cell and button

            const deleteCell = document.createElement('td');
            const deleteButton = document.createElement('button');
            deleteButton.textContent = 'DELETE';
            deleteButton.addEventListener('click', (e) => {
                const delIndex = templateToSend.findIndex((row) => {
                    row.id === e.target.closest('tr').id;
                });
                templateToSend.splice(delIndex, 1);
                upddateTable(table, template);
            });
            deleteCell.appendChild(deleteButton);
            row.appendChild(deleteCell);

            //TODO edit button

            tableBody.appendChild(row);
        });
    };
    upddateTable(tableBody, templateToSend);
});
