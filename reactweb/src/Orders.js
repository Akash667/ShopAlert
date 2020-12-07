import React from 'react';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import TextField from '@material-ui/core/TextField';
import Title from './Title';
import { Paper } from '@material-ui/core';
import { Button } from '@material-ui/core';

// Generate Order Data
function createData(id, date, name, shipTo, paymentMethod) {
  return { id, date, name, shipTo, paymentMethod };
}

const rows = [
  createData(0, '7 Dec, 2020', 'Samsung Galaxy M51 (Electric Blue, 6GB RAM, 128GB Storage)', '21,999', 'akashrawatcats@gmail.com'),
  createData(1, '5 Dec, 2020', 'MSI Gaming GL65 Leopard', '81,999', 'akashrawatcats@gmail.com'),
  createData(2, '1 Dec, 2020', 'OnePlus Y Series 80 cm ', '13,999', 'akashrawatcats@gmail.com'),
];

function preventDefault(event) {
  event.preventDefault();
}

const useStyles = makeStyles((theme) => ({
  seeMore: {
    marginTop: theme.spacing(3),
  },
  root: {
    display: 'flex',
    flexDirection: 'row',
    alignItem:'center'
  },
  end: {
    alignItem: 'flex-end'
  }
}));

export default function Orders() {
  const classes = useStyles();
  return (
    <React.Fragment>
      <Paper >
        <form className={classes.root} noValidate autoComplete="off">
          <TextField
            id="standard-full-width"
            label="Enter Product URL"
            style={{ margin: 8, width: '90%' }}
            placeholder="URL"
            helperText="Add your Amazon link"
            margin="normal"
            InputLabelProps={{
              shrink: true
            }}

          />
          <TextField id="standard-basic" label="Target Price" />
          <Button variant="contained" color="primary" onClick={() => {rows.push(createData(6, '8 Dec, 2020', 'New Apple MacBook Air (13-inch, 1.1GHz Dual-core 10th-Generation Intel Core i3 Processor, 8GB RAM, 256GB Storage) ', '83990', 'akashrawatcats@gmail.com'))}} >
            ADD
            </Button>
        </form>
      </Paper>
      <Title>Alerts</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>Date</TableCell>
            <TableCell>Product Name</TableCell>
            <TableCell>Target Price</TableCell>
            <TableCell>Email Address</TableCell>

          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.date}</TableCell>
              <TableCell>{row.name}</TableCell>
              <TableCell>{row.shipTo}</TableCell>
              <TableCell>{row.paymentMethod}</TableCell>

            </TableRow>
          ))}
        </TableBody>
      </Table>

    </React.Fragment>
  );
}
