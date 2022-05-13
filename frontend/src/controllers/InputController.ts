/* eslint-disable */
import { Metadata } from '@zeedhi/core';
import { Select } from '@zeedhi/common';
import axios, {AxiosResponse} from 'axios';

export class InputController {
    public data = [];
    public onMounted() {
        const headers = {
            "Content-Type": "application/json"
        };

        const getRequest = async () => {
            try {
                const resp = await axios.get('https://apimocha.com/brazasteste/products', { headers });
                console.log(resp);
            } catch (err) {
                console.log(err);
            }
        }
        getRequest();
    }

  get selectedItemObject() {
    const selectObject = Metadata.getInstance<Select>('objectSelectResult');
    const itemsText = (selectObject.value || '');
    return `selected value: ${JSON.stringify(itemsText)}`;
  }
}
