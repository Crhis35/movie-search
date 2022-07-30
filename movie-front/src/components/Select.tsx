import AsyncSelect from "react-select/async";

type CustomSelectProps = {
  loadOptions: (arg1: string, arg2: any) => void;
};

const CustomSelect = ({ loadOptions }: CustomSelectProps) => {
  return <AsyncSelect loadOptions={loadOptions} />;
};

export default CustomSelect;
