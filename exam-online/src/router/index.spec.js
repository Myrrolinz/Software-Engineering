import { shallowMount } from '@vue/test-utils';
import index from './index';





describe('<index/>', () => {
	const wrapper = shallowMount(index);

	// 快照测试
	it('snapshot测试', () => {
		const wrapper2 = shallowMount(index);
		expect(wrapper2).toMatchSnapshot()
		wrapper2.destroy()
    })

	
  });